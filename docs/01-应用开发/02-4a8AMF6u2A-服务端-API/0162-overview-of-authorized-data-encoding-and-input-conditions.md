---
title: "授权数据编码及入参条件概览"
source_url: "https://open.dingtalk.com/document/development/overview-of-authorized-data-encoding-and-input-conditions"
namespace: "development"
slug: "overview-of-authorized-data-encoding-and-input-conditions"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 上下级组织（原关联组织） > 授权数据编码及入参条件概览"
doc_id: "xz3h0medZg"
updated_at: "2025-12-05 17:32:38"
---

> Source: https://open.dingtalk.com/document/development/overview-of-authorized-data-encoding-and-input-conditions
> Path: 应用开发 / 服务端 API / 通讯录管理 > 上下级组织（原关联组织） > 授权数据编码及入参条件概览
> Updated: 2025-12-05 17:32:38

# 授权数据编码及入参条件概览

| 数据主类 | 数据子类 | body入参条件 | 子类数据编码 | 指标编码 | 指标名称 |
| --- | --- | --- | --- | --- | --- |
| 组织基础数据 | 组织 | "statDate": "yyyyMMdd"（必传） 如:"statDate":"20210509" 表示需要查询2021年5月9日那天的统计数据，入参时间仅限过去两周内的日期。 | GROUP\_GRO\_ORG\_OPEN\_ORG | CRO\_ORG\_OPEN\_EDU\_001 | 注册班级数。 |
| CRO\_ORG\_OPEN\_EDU\_002 | 活跃班级群数。 |
| 用户 | "statDate": "yyyyMMdd"（必传） 如:"statDate":"20210509" 表示需要查询2021年5月9日那天的统计数据，入参时间仅限过去两周内的日期。 | GROUP\_GRO\_ORG\_OPEN\_USER | CRO\_ORG\_OPEN\_EDU\_003 | 激活教师数。 |
| CRO\_ORG\_OPEN\_EDU\_004 | 激活学生数。 |
| CRO\_ORG\_OPEN\_EDU\_005 | 昨日活跃教师数。 |
| CRO\_ORG\_OPEN\_EDU\_006 | 近7日活跃教师数。 |
| CRO\_ORG\_OPEN\_EDU\_007 | 近30日活跃教师数。 |
| CRO\_ORG\_OPEN\_EDU\_008 | 昨日活跃学生数。 |
| CRO\_ORG\_OPEN\_EDU\_009 | 近7日活跃学生数。 |
| CRO\_ORG\_OPEN\_EDU\_010 | 近30日活跃学生数。 |
| CRO\_ORG\_OPEN\_EDU\_011 | 昨日日活跃家长数。 |
| CRO\_ORG\_OPEN\_EDU\_012 | 近7日活跃家长数。 |
| CRO\_ORG\_OPEN\_EDU\_013 | 近30日活跃家长数。 |
| 数字化指数 | 数字化指数 | "statDate": "yyyyMMdd"（必传） 如:"statDate":"20210509" 表示需要查询2021年5月9日那天的统计数据，入参时间仅限过去两周内的日期。 | GROUP\_GRO\_ORG\_OPEN\_INDEX | CRO\_ORG\_OPEN\_EDU\_078 | 数字化分。 |
| CRO\_ORG\_OPEN\_EDU\_079 | 班级管理。 |
| CRO\_ORG\_OPEN\_EDU\_080 | 学校管理。 |
| 应用使用数据 | 家校互动 | "statDate": "yyyyMMdd"（必传） 如:"statDate":"20210509" 表示需要查询2021年5月9日那天的统计数据，入参时间仅限过去两周内的日期。 | GROUP\_GRO\_ORG\_OPEN\_JXHD | CRO\_ORG\_OPEN\_EDU\_014 | 家校互动人数。 |
| 打卡 | "statDate": "yyyyMMdd"（必传） 如:"statDate":"20210509" 表示需要查询2021年5月9日那天的统计数据，入参时间仅限过去两周内的日期。 | GROUP\_GRO\_ORG\_OPEN\_CARD | CRO\_ORG\_OPEN\_EDU\_015 | 昨日打卡发布次数。 |
| CRO\_ORG\_OPEN\_EDU\_016 | 近7日打卡发布次数。 |
| CRO\_ORG\_OPEN\_EDU\_017 | 近30日打卡发布次数。 |
| CRO\_ORG\_OPEN\_EDU\_018 | 昨日 打卡使用人数。 |
| CRO\_ORG\_OPEN\_EDU\_019 | 近7日 打卡使用人数。 |
| CRO\_ORG\_OPEN\_EDU\_020 | 近30日 打卡使用人数。 |
| CRO\_ORG\_OPEN\_EDU\_021 | 昨日提交打卡次数。 |
| CRO\_ORG\_OPEN\_EDU\_022 | 近7日 提交打卡次数。 |
| CRO\_ORG\_OPEN\_EDU\_023 | 近30日 提交打卡次数。 |
| CRO\_ORG\_OPEN\_EDU\_024 | 昨日提交打卡人数。 |
| CRO\_ORG\_OPEN\_EDU\_025 | 近7日提交打卡人数。 |
| CRO\_ORG\_OPEN\_EDU\_026 | 近30日提交打卡人数。 |
| 教职工钉消息 | "statDate": "yyyyMMdd"（必传） 如:"statDate":"20210509" 表示需要查询2021年5月9日那天的统计数据，入参时间仅限过去两周内的日期。 | GROUP\_GRO\_ORG\_OPEN\_DING | CRO\_ORG\_OPEN\_EDU\_027 | 昨日教师钉使用人数。 |
| CRO\_ORG\_OPEN\_EDU\_028 | 近7日教师钉使用人数。 |
| CRO\_ORG\_OPEN\_EDU\_029 | 近30日教师钉使用人数。 |
| CRO\_ORG\_OPEN\_EDU\_030 | 昨日教师钉消息数。 |
| CRO\_ORG\_OPEN\_EDU\_031 | 近7日教师钉消息数。 |
| CRO\_ORG\_OPEN\_EDU\_032 | 近30日教师钉消息数。 |
| 班级圈 | "statDate": "yyyyMMdd"（必传） 如:"statDate":"20210509" 表示需要查询2021年5月9日那天的统计数据，入参时间仅限过去两周内的日期。 | GROUP\_GRO\_ORG\_OPEN\_CLASS | CRO\_ORG\_OPEN\_EDU\_033 | 昨日班级圈使用班级数。 |
| CRO\_ORG\_OPEN\_EDU\_034 | 近7日班级圈使用班级数。 |
| CRO\_ORG\_OPEN\_EDU\_035 | 近30日班级圈使用班级数。 |
| CRO\_ORG\_OPEN\_EDU\_036 | 昨日班级圈使用人数。 |
| CRO\_ORG\_OPEN\_EDU\_037 | 近7日班级圈使用人数。 |
| CRO\_ORG\_OPEN\_EDU\_038 | 近30日班级圈使用人数。 |
| CRO\_ORG\_OPEN\_EDU\_039 | 昨日通知使用班级数。 |
| CRO\_ORG\_OPEN\_EDU\_040 | 近7日通知使用班级数。 |
| CRO\_ORG\_OPEN\_EDU\_041 | 近30日通知使用班级数。 |
| CRO\_ORG\_OPEN\_EDU\_042 | 昨日通知发布次数。 |
| CRO\_ORG\_OPEN\_EDU\_043 | 近7日通知发布次数。 |
| CRO\_ORG\_OPEN\_EDU\_044 | 近30日通知发布次数。 |
| CRO\_ORG\_OPEN\_EDU\_045 | 昨日通知平均确认率。 |
| CRO\_ORG\_OPEN\_EDU\_046 | 近7日通知平均确认率。 |
| CRO\_ORG\_OPEN\_EDU\_047 | 近30日通知平均确认率。 |
| CRO\_ORG\_OPEN\_EDU\_048 | 昨日通知使用人数。 |
| CRO\_ORG\_OPEN\_EDU\_049 | 近7日通知使用人数。 |
| CRO\_ORG\_OPEN\_EDU\_050 | 近30日通知使用人数。 |
| 班级树 | "statDate": "yyyyMMdd"（必传） 如:"statDate":"20210509" 表示需要查询2021年5月9日那天的统计数据，入参时间仅限过去两周内的日期。 | GROUP\_GRO\_ORG\_OPEN\_CLASS\_TREE | CRO\_ORG\_OPEN\_EDU\_051 | 昨日班级树使用班级数。 |
| CRO\_ORG\_OPEN\_EDU\_052 | 近7日班级树使用班级数。 |
| CRO\_ORG\_OPEN\_EDU\_053 | 近30日班级树使用班级数。 |
| CRO\_ORG\_OPEN\_EDU\_054 | 昨日班级树使用人数。 |
| CRO\_ORG\_OPEN\_EDU\_055 | 近7日班级树使用人数。 |
| CRO\_ORG\_OPEN\_EDU\_056 | 近30日班级树使用人数。 |
| 填表 | "statDate": "yyyyMMdd"（必传） 如:"statDate":"20210509" 表示需要查询2021年5月9日那天的统计数据，入参时间仅限过去两周内的日期。 | GROUP\_GRO\_ORG\_OPEN\_FORM | CRO\_ORG\_OPEN\_EDU\_057 | 昨日填表使用班级数。 |
| CRO\_ORG\_OPEN\_EDU\_058 | 近7日填表使用班级数。 |
| CRO\_ORG\_OPEN\_EDU\_059 | 近30日填表使用班级数。 |
| CRO\_ORG\_OPEN\_EDU\_060 | 昨日填表发起次数。 |
| CRO\_ORG\_OPEN\_EDU\_061 | 近7日填表发起次数。 |
| CRO\_ORG\_OPEN\_EDU\_062 | 近30日填表发起次数。 |
| CRO\_ORG\_OPEN\_EDU\_063 | 昨日填表使用人数。 |
| CRO\_ORG\_OPEN\_EDU\_064 | 近7日填表使用人数。 |
| CRO\_ORG\_OPEN\_EDU\_065 | 近30日填表使用人数。 |
| 在线课堂 | "statDate": "yyyyMMdd"（必传） 如:"statDate":"20210509" 表示需要查询2021年5月9日那天的统计数据，入参时间仅限过去两周内的日期。 | GROUP\_GRO\_ORG\_OPEN\_ONCLASS | CRO\_ORG\_OPEN\_EDU\_066 | 昨日在线课堂课程数。 |
| CRO\_ORG\_OPEN\_EDU\_067 | 近7日在线课堂课程数。 |
| CRO\_ORG\_OPEN\_EDU\_068 | 近30日在线课堂课程数。 |
| CRO\_ORG\_OPEN\_EDU\_069 | 昨日在线课堂发起人数。 |
| CRO\_ORG\_OPEN\_EDU\_070 | 近7日在线课堂发起人数。 |
| CRO\_ORG\_OPEN\_EDU\_071 | 近30日在线课堂发起人数。 |
| CRO\_ORG\_OPEN\_EDU\_072 | 昨日在线课堂参与人数。 |
| CRO\_ORG\_OPEN\_EDU\_073 | 近7日在线课堂参与人数。 |
| CRO\_ORG\_OPEN\_EDU\_074 | 近30日在线课堂参与人数。 |
| CRO\_ORG\_OPEN\_EDU\_075 | 昨日在线课堂使用时长。 |
| CRO\_ORG\_OPEN\_EDU\_076 | 近7日在线课堂使用时长。 |
| CRO\_ORG\_OPEN\_EDU\_077 | 近30日在线课堂使用时长。 |
