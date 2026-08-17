---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/sdk-faq"
namespace: "development"
slug: "sdk-faq"
group: "硬件开发"
tab: "SDK 接入（通用）"
breadcrumb: "常见问题"
doc_id: "Kx1DP0pcDN"
updated_at: "2026-08-03 09:19:31"
---

> Source: https://open.dingtalk.com/document/development/sdk-faq
> Path: 硬件开发 / SDK 接入（通用） / 常见问题
> Updated: 2026-08-03 09:19:31

# 常见问题

SDK接入接口遇见的常见问题。

## **钉钉SDK接入（通用）**

- **本SDK是否提供网络接入能力？**

  目前发布的SDK为1.1版本，只提供了协助厂商进行WIFI配网的接口，暂未提供网络通讯能力，如果需要网络通讯能力，请直接参考阿里云IOT的LINK-SDK接入。
- **为什么蓝牙通讯使用物模型？**

  大部分具有网络通讯能力的接入设备，其网络部分采用的阿里云物联网接入开源方案，其使用的也是物模型协议，为了保持协议的一致性，本SDK蓝牙端也使用物模型作为蓝牙通讯上层协议。
- **51架构的单片机是否能够接入SDK？**

  目前版本的SDK需要动态内存分配能力，很多传统51单片机无法支持内存分配能力，不过这种类型的单片机目前已经不多了，如果有接入需要，可联系勤龙来评估具体接入开发。
- **具体我接入的设备的业务相关的物模型文档从哪里获取？**

  后续对应接入设备的物模型文档会和本SDK交付物一同提供。
- **SDK对系统资源的要求？**

  - SDK内部自己实现AES+MD5时， FLASH需要30K，RAM需要8K。
  - SDK内部不自己实现AES+MD5时，FLASHA需要20K，RAM需要4K。
- **每次蓝牙通讯数据的最大长度是多少？**

  最大长度1K。

## **钉钉门禁Linux SDK接入**

- **考勤记录时间偏差8小时？**

  确认下系统的时区是否设置，有些厂商不设置时区，但是为了让系统显示的时间与中国时区一致，故意在时间戳上加了8小时。

  如果是上述情况，请使用dtiot\_device\_service\_singleton()->set\_timezone(-480)，注意-480是东八区8\*60得出。
- **为什么有的人无法识别**

  确认算法服务器可以正确抽取此人此照片的特征，联系钉钉进行5W人脸抽特征压测，看是否有照片抽不出特征，如有请修改算法。
- **扫描二维码提示设备离线或者设备已绑定**

  请在确保设备到公网通的情况下调用dtiot\_netconfig\_bind\_service\_singleton()->static\_bind\_start，三方自行加一个外网监测。

  在一些设备中存在ping外网通，但是解析域名出错问题，请在设置或更新DNS后调用res\_init函数，具体原因可自行搜索查询。
- **解绑后重新绑定异常**

  解绑的时候请确保删除dtiot\_device\_service\_singleton()->set\_storage\_path设置的目录中的全部内容。
- **SDK连接钉钉服务器失败**

  确定设备的时钟是否同步，钉钉通信协议依赖系统时钟准确性。
- **用了达摩院人脸SDK，链接不通过，报std++错误**

  libidst-cv.so: undefined reference to `std::current\_exception()@CXXABI\_1.3.3'

  需要在LINK时，加上-mcpu=cortex-a7 选项。
- **sqlite冲突导致一运行就报CRASH**

  检查程序是否自己也链接了sqlite库，如果是，请去掉这个客户自己的SQLITE库，改用阿里SDK包中自带的SQLITEX库，这个库是SDK里要用到的，如果客户自己也链入一个SQLITE库，就会导致符号相同，实现不同，名字空间污染至CRASH。

  解决方案：

  抛弃客户自带的SQLITE库和头文件，采用阿里的SQLITE库，头文件指向SDK包的SQLITE目录。
