---
title: "SDK接入接口"
source_url: "https://open.dingtalk.com/document/development/sdk-access-interface"
namespace: "development"
slug: "sdk-access-interface"
group: "硬件开发"
tab: "SDK 接入（通用）"
breadcrumb: "SDK接入接口"
doc_id: "810oeVo9oR"
updated_at: "2026-08-03 09:19:30"
---

> Source: https://open.dingtalk.com/document/development/sdk-access-interface
> Path: 硬件开发 / SDK 接入（通用） / SDK接入接口
> Updated: 2026-08-03 09:19:30

# SDK接入接口

本文介绍了如何使用SDK接入接口。

## 蓝牙基础能力改造

### **设备广播数据**

SDK会回调三方进行广播，广播的数据放在Manufacture Data中, 蓝牙广播共31个字节，要求三方预留22个字节。进行广播回调的接口有start\_advertising, update\_advertising。接口中有广播的时间间隔，信号强度和广播内容。停止广播的接口为stop\_advertising。

> **[!IMPORTANT]**
>
> 广播的时候需要带上服务特征值的UUID。

| 字段 | LEN | TYPE | VALUE |
| --- | --- | --- | --- |
| TAG | 2 | 0x01 | 0x06 |
| UUID | 3 | 0x03 | 0xfe3c |
| Manufacturer Data | 22 | 0xFF | SDK通过回调接口传给接入厂商 |
| NAME | 31字节以内 | 0x09 | PRODUCT\_DEVICE\_NAME+设备SN |

### **服务特征值**

- **SERVICE\_UUID**：`{0xfb,0x34,0x9b,0x5f,0x80,0x00,0x00,0x80,0x00,0x10,0x00,0x00,0x3c,0xfe,0x00,0x00}`
- **SERVER\_TX\_UUID**：`{0xfb,0x34,0x9b,0x5f,0x80,0x00,0x00,0x80,0x00,0x10,0x00,0x00,0x1b,0xfe,0x00,0x00}`

  **属性**：NOTIFY, READ
- **SERVER\_RX\_UUID**：`{0xfb,0x34,0x9b,0x5f,0x80,0x00,0x00,0x80,0x00,0x10,0x00,0x00,0x1c,0xfe,0x00,0x00}`

  **属性**：WRITE, WRITE NO RESPONSE

### **蓝牙数据通讯**

厂商需要自己实现在您所接入产品平台上的蓝牙数据收发的基础能力，SDK帮您解析您收到的数据，并将解析后的数据以物模型定义好的JSON格式数据传给您。同时当您业务层需要向钉钉端通过蓝牙传输业务数据时，只要将封装好的物模型数据信息传给SDK，SDK会封装成钉钉内部的通讯格式通过您提供的蓝牙基础能力传给钉钉。

![蓝牙数据传输](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1669786061/p186366.png)

蓝牙数据通讯的交互流程图如下：

![BEB9444A-87C8-4276-8936-3BD979B7224D](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2306276061/p186369.png)

## 模块接入

### **dtiot\_device\_service接入**

dtiot\_device\_service模块主要提供和设备信息以及设备状态相关的接口能力。

1. **init接口**

   ```
   int (*init)(dtiot_product_info_t *product_info, 
                   const char *device_sn, 
                   const char *device_mac, 
                   const char *device_name, 
                   const char *device_secret);
   ```

   该函数为模块的初始化函数，通过本接口将设备相关信息注册给SDK。

   其中product\_info信息按照头文件的定义类型传入，无特殊情况，可参考示例demo中提供的配置信息传入即可。

   - **device\_sn**为您设备的SN信息，请保证每台设备具有唯一的SN信息。
   - **device\_mac**为您设备的蓝牙MAC信息，请保证每台设备具有唯一的MAC信息。

     ```
     typedef struct dtiot_product_info {
         int platform;
         int product_id;
         int net_devices;
         int bind_method;
         int qr_type;
         short product_type;
         char product_key[DTIOT_PRODUCT_KEY_LEN];
         char product_secret[DTIOT_PRODUCT_SECRET_LEN];   
         char product_sign[DTIOT_PRODUCT_SIGN_LEN];       
         char product_manufacturer_version[DTIOT_PRODUCT_MANUFACTURER_VERSION_LEN];
     } dtiot_product_info_t;
     ```

     product\_info信息与您向钉钉提前申请的信息对应关系如下，其他字段按照示例demo中的默认参数传递即可。

     | product\_key | PRODUCT\_KEY | 产品的蓝牙绑定接入密钥 |
     | --- | --- | --- |
     | product\_type | DTIOT\_DEV\_TYPE | 产品的接入类型 |
     | product\_id | DTIOT\_DEVICE\_SERVE\_ID | 产品的接入型号 |
2. **register\_bind\_listener接口**

   该接口为向SDK注册绑定状态的回调通知，当设备的绑定状态发生改变时，会通过该回调函数通知接入厂商。

   ```
   int (*register_bind_listener)(void (*bind_status_callback)(int status));
   ```
3. **get\_bind\_status接口**

   该接口为接入厂商主动调用来获取SDK当前的绑定状态信息，一般在系统启动的时候使用该接口来判断设备的当前状态。

   ```
   int (*get_bind_status)(void);
   ```
4. **unbind接口**

   该接口为接入设备主动向SDK发送解绑事件，完成设备的解绑操作。通常在带有复位键的设备上使用，当触发了设备复位操作时，通过本接口告知SDK设备并完成设备解绑操作。

   ```
   int (*unbind)(void);
   ```
5. **register\_set\_dev\_time接口**

   该函数为向SDK注册获取系统RTC时间戳的功能接口，SDK在每次蓝牙连接以及绑定成功后，会获取到手机发过来的当前时间戳，并通过这里注册的回调函数传给接入设备，并给接入设备同步时间。单位为秒。

   ```
   int (*register_set_dev_time)(int (*set_dev_time_callback)(unsigned int timestamp));
   ```

### **dtiot\_ble\_hal\_service接入**

1. **init接口**

   该函数用来初始化dtiot\_ble\_hal\_service模块，并向该模块注册相关的回调函数。

   ```
   struct dtiot_ble_hal_callback_s {
     int (*start_advertising)(int interval, int rssi_level, unsigned char *data, int len);
     int (*update_advertising)(int interval, int rssi_level, unsigned char *data, int len);
     int (*stop_advertising)();
     int (*notify_characteristic_changed)(unsigned char *data, int len);
   };
   ```

   其中：

   - **start\_advertising**函数为SDK通知接入设备，开始蓝牙广播，并将蓝牙广播中的厂商自定义字段数据内容通过该函数传给接入设备，接入设备按照传入的数据，开始蓝牙广播。
   - **update\_advertising**函数作用与start\_advertising类似，只是在需要更新广播数据的时候，会触发本回调函数。告知接入设备，按照传入的数据更新蓝牙广播。
   - **stop\_advertising**函数为通知接入设备，停止蓝牙广播。
   - **notify\_characteristic\_changed**函数为SDK调用接入设备的底层蓝牙能力，向外发送蓝牙数据。接入设备在处理该回调函数时，需要将SDK传过来的数据进行拆包，按照每包20字节进行分包发送。
2. **on\_characteristic\_write\_request接口**

   该函数为接入设备接收到蓝牙数据后，直接通过该接口透传给SDK。

   ```
   int (*on_characteristic_write_request)(unsigned char *data, int len);
   ```
3. **on\_ble\_connect\_state\_change接口**

   该接口为当蓝牙连接状态发生改变时，接入设备通过该接口告知SDK，SDK内部会根据蓝牙连接状态做一些内部变量的初始化操作。

   ```
   int (*on_ble_connect_state_change)(int state);
   ```

### **dtiot\_ble\_bind\_service接入**

该模块主要为蓝牙绑定相关以及物模型数据传输相关的接口封装。

1. **start接口**

   ```
   int (*start)(dtiot_ble_bind_callback_t *callback);
   ```

   该接口为对dtiot\_ble\_bind\_service模块的初始化接口，并通过该接口向SDK注册相关的回调函数如下：

   ```
   struct dtiot_ble_bind_callback_s {
     char* (*get_device_info)(void);
     int (*get_data)(char *data, int len);
     int (*auth_result)(int flag);
     int (*get_wifi_list)(void (*on_get_wifi_list)(char *data, int length));
     int (*connect_wifi)(char *ssid, char *password);
   };
   ```

   - **get\_device\_info**回调函数会返回设备的相关信息，在示例demo中返回的信息如下。

     ```
     {
       "pk":"7403bd61a2f442f7a0722c3f0c26ebcb",  -----这里即分发的 PRODUCT_KEY
       "dn":"DT112233445566",                    -----这里填写设备的实际SN
       "supportWifi":0,                          -----本字段标识接入设备是否支持WIFI配网
       "supportWire":0,                          -----本字段填写是否支持有线网络
       "supportgsm":0,                           -----本字段填写是否支持4G网络
       "code":200
     }
     ```
   - **get\_data**接口为当SDK收到物模型数据需要传递给接入设备时，会通过本接口传给接入设备

     该接口会接收到两类物模型数据，一类为钉钉端通过蓝牙主动给设备发送的物模型命令；还有一类为钉钉端通过蓝牙返回的设备端发送的物模型死命令的应答。
   - **auth\_result**接口为SDK告知接入设备当前设备是否处于安全模式，每次蓝牙连接成功后，钉钉端首先会与设备完成安全认证，只有安全认证通过后，SDK才会进入安全模式，否则处于非安全模式。当接入设备处于非安全模式时，请勿处理任务业务数据。
   - **get\_wifi\_list**接口为接入设备提供给SDK的获取WIFI列表的接口，只有当具有WIFI能力且需要SDK提供配网能力的场景下才会使用本接口。

     获取设备侧的wifi 列表，列表为json数组的字符串，返回给SDK为字符串的长度和内容

     单个wifi的json如下，具体可参考示例DEMO中的示例数据。

     ```
     [{  "ssid": "xxx", "isOpen": 1}]
     ```
   - **connect\_wifi**接口为连接目标WIFI设备的回调，接入设备收到该回调来连接目标WIFI，传输的数据格式如下：

     ```
     "{\"ssid\":\"huawei\",\"password\":\"12345678\"}";
     ```
2. **send\_data接口**

   接入设备通过本接口来发送物模型主动上报数据，如设备主动发起的属性上报，事件上报等物模型数，均调用本接口处理。

   ```
   void (*send_data)(char *data, int len);
   ```
3. **send\_response接口**

   接入设备收到SDK传过来的物模型命令，处理完毕后通过本接口发送物模型的处理结果应答数据。

   ```
   void (*send_response)(char *data, int len);
   ```
4. **data\_sync\_over接口**

   当接入设备在业务场景下通过物模型上报同步本地属性完成的时候，通过本接口告知SDK数据同步已经完成。

   ```
   void (*data_sync_over)(void);
   ```
5. **data\_event接口**

   本接口为接入设备发生超时，或者相关业务结束时候，通过本接口告知SDK。

   ```
   int (*data_event)(int type);
   ```

   目前支持的事件类型主要有：

   ```
   typedef enum {
     BIND_BLE_EVENT_DEV_LOCKED,
     BIND_BLE_EVENT_DEV_TIMEOUT, 
     BIND_BLE_WIFI_STATE_NONE,
     BIND_BLE_WIFI_STATE_CONNECTING,
     BIND_BLE_WIFI_STATE_SUCCESS,
     BIND_BLE_WIFI_STATE_PASSWORD_ERR,
     BIND_BLE_WIFI_STATE_TIMEOUT,
   } dtiot_bind_service_ble_event_e;
   ```

## dtiot\_os\_hal模块实现

该文件为SDK所依赖的OS层相关功能函数，因SDK为标准接入SDK其可适配各种不同的平台，因此为了最大化SDK的平台兼容性，针对不同平台系统底层的能力，需要依赖接入厂商来实现一些基础功能单元。

> **[!IMPORTANT]**
>
> 提供给厂商的文件中实现的函数均为SDK内部使用的函数，请不要修改函数定义，接入厂商只要根据自己平台，改变函数的实现即可。

1. **内存分配相关接口**

   内存分配与释放函数接口实现，接入厂商请根据自己平台重构内存分配和释放函数，分配时要记得要清零即将分配的内存**memset**成0。

   ```
   extern void *dt_malloc0(size_t sz);
   extern void dt_free(void *ptr);
   ```
2. **数据读写相关功能函数**

   请在内部或者外部FLASH中，给SDK开辟一块由SDK单独使用的存储空间，空间大小不会超过4K。

   通常SDK传参过来的起始地址默认从0开始，厂商根据自己分配的地址空间，做个转换即可。例如，厂商分配0x10000 ~ 0x11000 空间给SDK，则当SDK传过来的address为0时，即代表实际地址的0x10000。

   ```
   extern int dtiot_data_write(int address, unsigned char *data, int len);
   extern int dtiot_data_read(int address, unsigned char *data, int len);
   ```
3. **安全加密相关功能函数 （随机数，加密，解密，HASH等）**

   接入设备收到SDK传过来的物模型命令，处理完毕后通过本接口发送物模型的处理结果应答数据。

   ```
   extern int dtiot_os_hal_aes(int en_flag, int sec_len, const unsigned char *key, const unsigned char *iv, int len, unsigned char *in, unsigned char *out);
   extern int dtiot_os_hal_md5(unsigned char *in, int len, unsigned char *out);
   ```

   另外两个密码算法AES 和HASH算法 MD5模块，默认在SDK中自行实现，但是会消耗额外的内存和FALSH存储空间，如果厂商本身平台产品已经具备上述两个算法，可以联系SDK维护人员提供内部不包含上述两个算法的SDK以减少SDK对资源的重复消耗。

   涉及到的资源情况如下：

   | 模块 | FLASH | RAM |
   | --- | --- | --- |
   | md5 | 3.5K | 200 |
   | aes | 3.2K | 3.5K |

   即如果SDK内部不自行实现AES与MD5算法，SDK可以减少7K左右的FALSH空间，4K左右的内存空间。

   SDK默认情况下，内部会自己实现AES与MD5功能，在此情况下，接入厂商无需实现

   - dtiot\_os\_hal\_aes
   - dtiot\_os\_hal\_md5

     如果接入厂商因为本身芯片资源紧张而需要SDK节省一部分资源，则可提供不带AES与MD5算法的SDK库，这样接入厂商就要自行实现上述两个功能函数。
4. **打印信息**

   SDK内部所有日志打印均调用上述三个接口函数，接入厂商需要根据自己平台的打印实际接口，采用上述接口进行二次封装供SDK内部使用。

   ```
   extern void INF(const char* format, ...);
   extern void ERR(const char* format, ...);
   extern void TRA(const char* format, ...);
   ```
