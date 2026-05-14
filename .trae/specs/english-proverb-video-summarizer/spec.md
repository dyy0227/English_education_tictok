# 英语熟语视频总结程序 - 产品需求文档

## Overview
- **Summary**: 开发一个自动化程序，从指定文件夹的英语视频中识别并提取各类英语熟语（Proverb、Saying、Colloquialism、Slang、Collocation、Phrasal verb、Set phrase），生成带中英文字幕的视频切片，并将相关信息存储到SQL数据库中。
- **Purpose**: 帮助英语学习者高效地从视频中学习真实场景下的英语熟语用法，提供可视化的学习素材。
- **Target Users**: 英语学习者、语言教师、内容创作者

## Goals
- 自动从视频中识别并提取7类英语熟语
- 生成带中英文字幕的视频切片
- 将熟语切片信息存储到SQL数据库
- 支持用户自定义配置（词数限制、LLM API选择等）
- 在保证质量的同时尽量节省API使用费用

## Non-Goals (Out of Scope)
- 不提供视频编辑功能
- 不支持实时视频处理
- 不提供视频上传或分享功能
- 不支持非英语视频

## Background & Context
- 参考项目：https://github.com/dyy0227/video_translate.git
- 使用Whisper进行语音转文字
- 使用FFmpeg进行视频处理
- 使用LLM（支持Ollama）进行熟语识别和翻译
- 需要处理大量视频文件，需考虑性能和成本优化

## Functional Requirements
- **FR-1**: 扫描指定文件夹，识别所有视频文件
- **FR-2**: 使用Whisper提取视频音频并转写为文字
- **FR-3**: 使用LLM识别文本中的熟语（Proverb、Saying、Colloquialism、Slang、Collocation、Phrasal verb、Set phrase）
- **FR-4**: 生成中英文字幕
- **FR-5**: 截取包含熟语的视频片段
- **FR-6**: 按熟语类型分类保存视频切片
- **FR-7**: 将熟语信息（切片位置、来源、长度等）写入SQL数据库
- **FR-8**: 支持用户配置（词数限制、LLM API、费用限制等）

## Non-Functional Requirements
- **NFR-1**: 支持Ollama本地LLM以节省API费用
- **NFR-2**: 支持批量处理视频文件
- **NFR-3**: 提供详细的处理日志和CLI进度报告
- **NFR-4**: 支持断点续处理
- **NFR-5**: 错误处理和异常恢复
- **NFR-6**: 支持GPU加速以提高处理速度（支持NVIDIA CUDA和AMD ROCm）

## Constraints
- **Technical**: Python 3.10+, 需要安装FFmpeg、Whisper、SQLite、MySQL等依赖
- **Business**: 需要控制API调用成本
- **Dependencies**: 需要额外下载的软件包（如Whisper模型、FFmpeg）

## Assumptions
- 用户已安装必要的依赖软件（FFmpeg等）
- 用户有可用的LLM API或已配置Ollama
- 视频文件格式为常见格式（MP4、AVI、MKV等）
- 用户有足够的存储空间保存视频切片

## Acceptance Criteria

### AC-1: 视频文件扫描
- **Given**: 指定包含视频文件的文件夹路径
- **When**: 程序启动扫描
- **Then**: 正确识别所有支持的视频文件并列出
- **Verification**: `programmatic`

### AC-2: 语音转文字
- **Given**: 视频文件和Whisper模型已安装
- **When**: 执行语音转文字处理
- **Then**: 生成包含时间戳的文本转录结果
- **Verification**: `programmatic`

### AC-3: 熟语识别
- **Given**: 转录文本和LLM API已配置
- **When**: 执行熟语识别
- **Then**: 正确识别并分类7类熟语
- **Verification**: `human-judgment`

### AC-4: 字幕生成
- **Given**: 识别出的熟语及上下文
- **When**: 执行翻译和字幕生成
- **Then**: 生成中英文字幕文件（SRT格式）
- **Verification**: `human-judgment`

### AC-5: 视频切片
- **Given**: 熟语时间戳和源视频
- **When**: 执行视频截取
- **Then**: 生成包含中英文字幕的视频切片
- **Verification**: `human-judgment`

### AC-6: 分类保存
- **Given**: 视频切片和熟语分类
- **When**: 执行保存操作
- **Then**: 按熟语类型分类保存到对应文件夹
- **Verification**: `programmatic`

### AC-7: SQL数据库更新
- **Given**: 熟语切片信息
- **When**: 执行数据库更新
- **Then**: 正确记录熟语、切片路径、来源、长度等信息
- **Verification**: `programmatic`

### AC-8: 用户配置
- **Given**: 用户设置文件
- **When**: 程序读取配置
- **Then**: 正确应用词数限制、LLM选择等配置
- **Verification**: `programmatic`

### AC-9: 成本控制
- **Given**: API费用限制配置
- **When**: 执行批量处理
- **Then**: 在费用限制内完成处理或提前终止
- **Verification**: `programmatic`

## Open Questions
- [x] 是否需要支持GPU加速？→ 是，已添加NFR-6
- [x] 是否需要提供图形界面？→ 否，CLI即可
- [x] 是否需要支持其他数据库类型（如MySQL）？→ 是，支持MySQL和SQLite
- [x] 是否需要提供进度报告功能？→ 是，已添加到NFR-3