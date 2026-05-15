# 英语熟语视频总结程序 - 实现计划

## [x] Task 1: 项目结构设计与初始化
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 创建项目目录结构
  - 初始化Python项目（requirements.txt）
  - 创建配置文件模板
- **Acceptance Criteria Addressed**: [AC-8]
- **Test Requirements**:
  - `programmatic` TR-1.1: 项目目录结构正确创建
  - `programmatic` TR-1.2: requirements.txt包含所有必要依赖
  - `human-judgment` TR-1.3: 配置文件模板完整合理
- **Notes**: 需要包含whisper、ffmpeg-python、ollama、sqlite3等依赖

## [x] Task 2: 视频文件扫描模块
- **Priority**: P0
- **Depends On**: Task 1
- **Description**: 
  - 实现视频文件扫描功能
  - 支持常见视频格式（MP4、AVI、MKV、MOV等）
  - 返回视频文件列表及其元数据
- **Acceptance Criteria Addressed**: [AC-1]
- **Test Requirements**:
  - `programmatic` TR-2.1: 正确扫描指定文件夹
  - `programmatic` TR-2.2: 正确识别视频文件格式
  - `programmatic` TR-2.3: 返回完整的视频元数据
- **Notes**: 使用glob或os.walk进行文件扫描

## [x] Task 3: 语音转文字模块（Whisper）
- **Priority**: P0
- **Depends On**: Task 1
- **Description**: 
  - 使用Whisper提取视频音频并转写
  - 生成带时间戳的转录结果
  - 支持模型选择（tiny/base/small/medium/large）
  - 支持GPU加速（NVIDIA CUDA和AMD ROCm）
- **Acceptance Criteria Addressed**: [AC-2]
- **Test Requirements**:
  - `programmatic` TR-3.1: 成功提取音频并转写
  - `programmatic` TR-3.2: 转录结果包含准确时间戳
  - `programmatic` TR-3.3: NVIDIA CUDA加速正常工作
  - `programmatic` TR-3.4: AMD ROCm加速正常工作
  - `human-judgment` TR-3.5: 转录质量符合预期
- **Notes**: 使用faster-whisper提高性能，支持AMD GPU

## [x] Task 4: LLM熟语识别模块
- **Priority**: P0
- **Depends On**: Task 1, Task 3
- **Description**: 
  - 实现Ollama API调用
  - 识别7类熟语（Proverb、Saying、Colloquialism、Slang、Collocation、Phrasal verb、Set phrase）
  - 返回熟语及其上下文和时间戳
- **Acceptance Criteria Addressed**: [AC-3]
- **Test Requirements**:
  - `programmatic` TR-4.1: 成功连接Ollama
  - `programmatic` TR-4.2: 返回结构化的熟语识别结果
  - `human-judgment` TR-4.3: 熟语识别准确率高
- **Notes**: 优化prompt以减少token消耗

## [x] Task 5: 字幕生成模块
- **Priority**: P0
- **Depends On**: Task 4
- **Description**: 
  - 使用LLM翻译熟语为中文
  - 生成SRT格式中英文字幕
  - 支持时间戳对齐
- **Acceptance Criteria Addressed**: [AC-4]
- **Test Requirements**:
  - `programmatic` TR-5.1: 成功生成SRT字幕文件
  - `programmatic` TR-5.2: 字幕时间戳与视频同步
  - `human-judgment` TR-5.3: 翻译质量准确自然
- **Notes**: 复用熟语识别的LLM调用以节省费用

## [x] Task 6: 视频切片模块（FFmpeg）
- **Priority**: P0
- **Depends On**: Task 2, Task 5
- **Description**: 
  - 使用FFmpeg截取视频片段
  - 添加中英文字幕
  - 支持多种输出格式
- **Acceptance Criteria Addressed**: [AC-5]
- **Test Requirements**:
  - `programmatic` TR-6.1: 成功截取视频片段
  - `programmatic` TR-6.2: 字幕正确嵌入视频
  - `human-judgment` TR-6.3: 视频切片质量良好
- **Notes**: 使用ffmpeg-python库

## [x] Task 7: 分类保存模块
- **Priority**: P0
- **Depends On**: Task 6
- **Description**: 
  - 按熟语类型创建文件夹
  - 将视频切片分类保存
  - 生成索引文件
- **Acceptance Criteria Addressed**: [AC-6]
- **Test Requirements**:
  - `programmatic` TR-7.1: 正确创建分类文件夹
  - `programmatic` TR-7.2: 视频切片保存到正确位置
  - `programmatic` TR-7.3: 生成完整的索引文件
- **Notes**: 熟语类型包括：Proverb、Saying、Colloquialism、Slang、Collocation、Phrasal verb、Set phrase

## [x] Task 8: SQL数据库模块
- **Priority**: P0
- **Depends On**: Task 1, Task 7
- **Description**: 
  - 设计数据库表结构
  - 实现数据插入和查询功能
  - 记录熟语信息、切片路径、来源、长度等
  - 支持SQLite和MySQL数据库
- **Acceptance Criteria Addressed**: [AC-7]
- **Test Requirements**:
  - `programmatic` TR-8.1: 数据库表正确创建
  - `programmatic` TR-8.2: 数据正确插入
  - `programmatic` TR-8.3: 查询功能正常工作
  - `programmatic` TR-8.4: SQLite连接正常
  - `programmatic` TR-8.5: MySQL连接正常
- **Notes**: 使用SQLite作为默认数据库，支持MySQL配置

## [x] Task 9: 用户配置模块
- **Priority**: P1
- **Depends On**: Task 1
- **Description**: 
  - 实现配置文件读取
  - 支持词数限制配置
  - 支持LLM API选择（Ollama/OpenAI等）
  - 支持费用限制配置
  - 支持外部依赖路径配置
- **Acceptance Criteria Addressed**: [AC-8]
- **Test Requirements**:
  - `programmatic` TR-9.1: 配置文件正确解析
  - `programmatic` TR-9.2: 配置参数正确应用
  - `human-judgment` TR-9.3: 配置界面友好
- **Notes**: 使用YAML格式配置文件

## [x] Task 10: 成本控制模块
- **Priority**: P1
- **Depends On**: Task 4, Task 9
- **Description**: 
  - 实现API调用计数
  - 实现费用估算
  - 支持费用限制和自动停止
- **Acceptance Criteria Addressed**: [AC-9]
- **Test Requirements**:
  - `programmatic` TR-10.1: 正确计数API调用
  - `programmatic` TR-10.2: 费用估算准确
  - `programmatic` TR-10.3: 达到费用限制时自动停止
- **Notes**: 需要定期更新费用统计

## [x] Task 11: 主程序整合
- **Priority**: P0
- **Depends On**: All previous tasks
- **Description**: 
  - 创建主程序入口（CLI）
  - 整合所有模块
  - 实现批量处理流程
  - 实现CLI进度报告功能
- **Acceptance Criteria Addressed**: [AC-1, AC-2, AC-3, AC-4, AC-5, AC-6, AC-7]
- **Test Requirements**:
  - `programmatic` TR-11.1: 主程序正常启动
  - `programmatic` TR-11.2: 批量处理流程完整执行
  - `programmatic` TR-11.3: CLI进度报告正常显示
  - `human-judgment` TR-11.4: 用户体验良好
- **Notes**: 添加详细的日志输出和CLI进度条

## [ ] Task 12: 测试与文档
- **Priority**: P2
- **Depends On**: All previous tasks
- **Description**: 
  - 编写单元测试
  - 创建使用文档
  - 添加示例配置
- **Acceptance Criteria Addressed**: [All]
- **Test Requirements**:
  - `programmatic` TR-12.1: 单元测试覆盖率达到60%
  - `human-judgment` TR-12.2: 文档完整清晰
- **Notes**: 使用pytest进行测试