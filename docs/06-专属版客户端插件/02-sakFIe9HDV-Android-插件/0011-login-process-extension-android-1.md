---
title: "登录流程扩展（Android）"
source_url: "https://open.dingtalk.com/document/development/login-process-extension-android-1"
namespace: "development"
slug: "login-process-extension-android-1"
group: "专属版客户端插件"
tab: "Android 插件"
breadcrumb: "使用扩展点 > 登录流程扩展"
doc_id: "zznWtIfwPD"
updated_at: "2025-10-15 17:02:20"
---

> Source: https://open.dingtalk.com/document/development/login-process-extension-android-1
> Path: 专属版客户端插件 / Android 插件 / 使用扩展点 > 登录流程扩展
> Updated: 2025-10-15 17:02:20

# 登录流程扩展（Android）

## **基础信息**

| **扩展点编码** | **接口类** | **支持的平台** |
| --- | --- | --- |
| login\_nodes | EpLoginNode | Android |

## **功能说明**

可用于在登录流程中扩展自定义节点。

> **[!IMPORTANT]**
>
> 由于该节点会直接阻塞钉钉登录流程，属于极度敏感的扩展点，因此请务必做好代码参数校验、健壮性设计，务必保证所有场景均调用了登录流程的Callback，将流程交换给钉钉平台。

> **[!NOTE]**
>
> - 当钉钉登录成功并杀进程重启App，仅会执行常规的Application.onCreate()生命周期事件，不会重走登录流程，即不会触发调用EpLoginNode节点。
> - 重启场景可在Application.onCreate()初始化回调中使用开放API，先判断账号登录状态，然后补偿插件相关的逻辑调用。

## **接口说明**

| **名称** | **说明** |
| --- | --- |
| setLoginContext() | 钉钉登录上下文，包括Activity等相关属性，可用于注册onActivityResult回调事件。 |
| getNodeType() | 登录节点的类型。   - NodeType.Prepare：登录前置准备节点，此时并不会产生uid等数据**（请注意，该类型暂不支持专属账号）。** - NodeType.Auth：身份验证环节节点，该节点将会在钉钉登录验证成功后调用，允许插入二次验证环节。 |
| bindData() | 执行execute前回调，可以在此获取必要的账号等信息数据。 |
| execute() | 节点执行体。   - onSuccess代表节点成功，继续回到钉钉登录流程中； - onException代表节点失败，中断登录流程回到登录页，第一个参数为code，第二个参数为msg，返回后钉钉会弹出Dialog，展示内容为msg（如果不为空）。   **[!IMPORTANT]**  请务必注意节点不要造成Crash，同时任何执行流程无论成功与否，均通过callback回调将登录流程交还给钉钉平台。 |

## **代码示例**

Java

```
@Extension(id="example_loginnode", target="login_nodes")
public class PrepareNode extends EpLoginNode {

    private LoginContext loginContext;
    private LoginData data;

		// 简化演示记录登录回调，activity可回调返回钉钉登录流程
		// 实际使用中建议定义Manager等做更优雅的封装
		public static ApiCallback<Void> loginFlowCallback;

    @Override
    public void setLoginContext(LoginContext context) {
        this.loginContext = context;
    }

    @Override
    public NodeType getNodeType() {
        return NodeType.Prepare;
    }

    @Override
    public void bindData(LoginData data) {
        this.data = data;
    }

    @Override
    public void execute(ApiCallback<Void> callback) {
        if (loginContext == null || loginContext.getActivity() == null) {
            callback.onException("100", "context invalid");
            return;
        }

				loginFlowCallback = callback;

        Intent intent = new Intent(loginContext.getActivity(), DemoActivity.class);
        loginContext.getActivity().startActivityForResult(intent, 10086);
        loginContext.registerActivityResult(10086, new EpLoginNode.OnActivityResultListener() {

            @Override
            public void onActivityResult(int requestCode, int resultCode, Intent data) {
                ToastUtils.show(loginContext.getActivity(), "node get activity result");
            }
        });
    }
}

// 自定义activity节点

public class DemoActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.demo_activity);
        
        findViewById(R.id.btn_success).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (PrepareNode.loginFlowCallback != null) {
                    PrepareNode.loginFlowCallback.onSuccess(null);
                }
                finish();
            }
        });

        findViewById(R.id.btn_error).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (PrepareNode.loginFlowCallback != null) {
                    PrepareNode.loginFlowCallback.onException("10", "prepare失败！");
                }
                finish();
            }
        });
    }
}
```
