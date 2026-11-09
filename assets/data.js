window.PORTFOLIO_DATA = {
  "profile": {
    "name": "Keji Yin",
    "subtitle": "Python · Data · AI Workflows",
    "degree": "Business Information Systems / Business Management",
    "githubUsername": "keji7-prog",
    "contactEmail": "",
    "about": "以商业信息系统为基础，持续学习 Python、数据分析与 AI 辅助工作流。关注技术如何帮助理解问题、组织信息和交付更清晰的成果。"
  },
  "projects": [
    {
      "id": "housing",
      "day": "22",
      "category": "采集与分析",
      "english": "HOUSING DATA",
      "title": "成都房源 · 2,040条实证分析",
      "intro": "读取课件 Excel 的 2,040 条成都历史挂牌记录，执行数值解析、数据核验与动态筛选统计。",
      "context": "将零散的二手房页面信息整理成便于查询和比较的数据表，是从采集到交付的一次完整课堂练习。",
      "process": [
        "分析页面结构及可读取的字段",
        "组织多页采集与数据解析代码",
        "将采集结果整理为结构化记录",
        "检查原始输出与展示层的衔接"
      ],
      "output": "以 2,040 条有效房源数值、可交互统计图、去识别 CSV 与标准库 Python 复核脚本为实证输出。原始课程爬虫没有在这次重新联网运行。",
      "skills": [
        "Python",
        "数据采集",
        "Excel",
        "数据整理"
      ],
      "status": "数据处理已执行",
      "demo": "housing.html",
      "links": [
        [
          "查看多页采集代码",
          "examples/day22/demo4多页数据获取.py"
        ],
        [
          "查看基础采集代码",
          "examples/day22/demo1贝壳二手房数据获取.py"
        ]
      ],
      "note": "来源：Day 22 课堂附件完整版贝壳二手房.xlsx（成都，历史挂牌快照）。Excel 数据已读取并分析；爬虫未重新联网运行。"
    },
    {
      "id": "freelance",
      "day": "15",
      "category": "采集与分析",
      "english": "FREELANCE RESEARCH",
      "title": "自由职业需求 · 关键词筛选",
      "intro": "以关键词、项目类别和记录字段为线索，整理程序员兼职需求信息。",
      "context": "将抓取脚本与业务问题连接起来：先定义希望了解的服务与技术方向，再组织搜索与 CSV 输出。",
      "process": [
        "围绕研究问题设计关键词",
        "分析不同站点的数据字段",
        "对结果进行结构化整理",
        "为趋势比较和业务分析做准备"
      ],
      "output": "收录两段对应课程采集脚本；原始平台记录与账号信息不直接公开。",
      "skills": [
        "Python",
        "关键词检索",
        "CSV",
        "业务分析"
      ],
      "status": "原始采集待复现",
      "demo": "",
      "links": [
        [
          "关键词采集代码",
          "examples/day15/demo1一个关键词数据获取.py"
        ],
        [
          "多来源案例代码",
          "examples/day15/demo3猿急送数据获取.py"
        ]
      ],
      "note": "来源：Day 15 课程代码，结果可能随站点变化。"
    },
    {
      "id": "csvlab",
      "day": "21",
      "category": "可视化",
      "english": "CSV DATA LAB",
      "title": "CSV 数据探索 · 浏览器演示版",
      "intro": "上传本地 CSV，在浏览器里检查字段、记录数量和数值列。",
      "context": "在 Day 20–21 图表课基础上，为这份作品集新增一个不依赖服务器的交互演示。展示从原始表格到可阅读摘要的基本流程。",
      "process": [
        "读取用户本地选择的 CSV 文件",
        "识别表头、行数与基本字段",
        "提取数值列并展示简易分布",
        "不将文件上传到任何服务端"
      ],
      "output": "已对课堂配发的 30,000 条模拟岗位数据实际计算分类中位时薪、均值及城市/月份指标；模拟性质已明确展示。另保留通用 CSV 上传实验室。",
      "skills": [
        "JavaScript",
        "CSV",
        "数据清洗",
        "交互设计"
      ],
      "status": "作品集整合演示",
      "demo": "results.html#jobs",
      "links": [
        [
          "打开 CSV 实验室",
          "demos/csv-lab.html"
        ],
        [
          "Day 20 数据处理代码",
          "examples/day20/demo02数据处理.py"
        ]
      ],
      "note": "浏览器演示为本次整理新制作，课程中的相关基础见 Day 20–21。"
    },
    {
      "id": "exams",
      "day": "19–20",
      "category": "可视化",
      "english": "ADMISSION CHARTS",
      "title": "院校数据 · 清洗与可视化",
      "intro": "围绕院校历年数据进行字段处理、分组对照与动态图表表达。",
      "context": "从 Day 19 的数据采集与整理，延续到 Day 20 的 Pyecharts 可视化输出，体现两个学习阶段之间的联系。",
      "process": [
        "读取采集得到的结构化表",
        "核对字段和缺失值",
        "编排图表并导出 HTML",
        "审查图表与数据口径"
      ],
      "output": "对课程 CSV 实际执行统计：5,580 行输入、20校、2023–2026 四个年份，识别到 137 行完全重复记录；提供可筛选学校/年份的图表和原始源文件校验值。",
      "skills": [
        "Pandas",
        "Pyecharts",
        "HTML",
        "数据表达"
      ],
      "status": "课程实践",
      "demo": "results.html#exams",
      "links": [
        [
          "数据处理示例",
          "examples/day20/demo02数据处理.py"
        ],
        [
          "绘图源码",
          "examples/day20/demo03可视化绘图.py"
        ]
      ],
      "note": "Day 20 课堂 CSV，未经外部官方核验；Day 19 部分错标文件已排除。"
    },
    {
      "id": "desktop",
      "day": "24",
      "category": "桌面应用",
      "english": "DESKTOP UTILITIES",
      "title": "六合一桌面工具 · Tkinter 练习集",
      "intro": "将计算器、截图、便签、倒计时、学习计时器与悬浮时钟组织在统一入口。",
      "context": "从一个简单 Tkinter 窗口扩展到多个独立脚本，再通过工具中心统一启动，是窗口、事件和程序组织的课程复盘。",
      "process": [
        "拆分六类日常桌面功能",
        "组织 Tkinter 控件与用户交互",
        "使用工具入口启动独立脚本",
        "保留不同版本以观察功能迭代"
      ],
      "output": "原计算器在 Linux Xvfb 真实运行发现裁切问题；AI 协助修正版已运行并通过 5/5 交互测试；原始便签关闭保存也已实测。Windows EXE 未验证。",
      "skills": [
        "Tkinter",
        "Python",
        "桌面交互",
        "脚本集成"
      ],
      "status": "部分 GUI 已实际运行",
      "demo": "desktop.html",
      "links": [
        [
          "查看工具中心代码",
          "examples/day24/六合一工具集成(1).py"
        ],
        [
          "查看截图工具代码",
          "examples/day24/简易截图工具(1).py"
        ]
      ],
      "note": "来源：Day 24 课堂 Python 练习。已做部分 Linux Tk GUI 和便签文件输出验证；完整 Windows 六合一仍待验证。"
    },
    {
      "id": "automation",
      "day": "13–18",
      "category": "自动化",
      "english": "BROWSER AUTOMATION",
      "title": "浏览器自动化与任务调度",
      "intro": "整理浏览器动态交互、请求结构、线程控制及周期性任务的基础练习。",
      "context": "这组课程围绕动态网站的页面元素、登录态及反爬机制展开；公开部分聚焦一般技术方法与安全的基础示例。",
      "process": [
        "识别静态/动态内容的区别",
        "理解浏览器自动化操作流程",
        "学习多线程和定时执行概念",
        "记录网站规则、凭据与反爬风险"
      ],
      "output": "仅提供经过筛选的学习代码；包含 Cookie、密钥、验证脚本等的原始资料未直接上传。",
      "skills": [
        "DrissionPage",
        "Requests",
        "线程",
        "任务调度"
      ],
      "status": "联网执行待复核",
      "demo": "",
      "links": [
        [
          "浏览器自动化示例",
          "examples/day13/demo1百度图片自动化批量下载.py"
        ],
        [
          "线程基础示例",
          "examples/day17/demo4单线程和多线程.py"
        ]
      ],
      "note": "来源：Day 13–18 课程。部分涉及第三方服务，不进行未授权抓取。"
    }
  ],
  "days": [
    {
      "day": 1,
      "title": "Python 基础与开发环境",
      "topics": "变量、输入输出、基础代码结构",
      "category": "编程基础",
      "summary": "从脚本最基本的读写和执行流程开始。",
      "sources": [
        "examples/day01/demo1.py",
        "examples/day01/demo4.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 2,
      "title": "条件判断与缘分检测器",
      "topics": "if / elif / else、交互输入",
      "category": "编程基础",
      "summary": "把分支判断组织成可运行的趣味练习。",
      "sources": [
        "examples/day02/Demo1.py",
        "examples/day02/Demo4.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 3,
      "title": "循环与拼夕夕模拟器",
      "topics": "for、循环嵌套、break / continue",
      "category": "编程基础",
      "summary": "理解重复执行与终止条件。",
      "sources": [
        "examples/day03/demo1 for循环基本用法.py",
        "examples/day03/demo4砍价自动停止版.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 4,
      "title": "列表字典与盲盒抽卡",
      "topics": "列表、字典、文件保存",
      "category": "编程基础",
      "summary": "用数据结构保存和管理模拟抽卡结果。",
      "sources": [
        "examples/day04/demo3字典的用法.py",
        "examples/day04/demo5盲盒数据保存.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 5,
      "title": "函数化与会员抽卡",
      "topics": "函数、参数、程序拆分",
      "category": "编程基础",
      "summary": "把规则封装为可复用函数。",
      "sources": [
        "examples/day05/demo1函数的基础使用.py",
        "examples/day05/demo4保存会员抽卡数据.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 6,
      "title": "人生模拟器",
      "topics": "全局变量、状态控制、流程组织",
      "category": "编程基础",
      "summary": "通过情景模拟理解程序状态。",
      "sources": [
        "examples/day06/demo1人生模拟器.py",
        "examples/day06/demo2global的使用.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 7,
      "title": "静态页面采集入门",
      "topics": "requests、HTML、图片下载",
      "category": "数据采集",
      "summary": "认识请求、响应及页面资源。",
      "sources": [
        "examples/day07/demo1爬虫体验.py",
        "examples/day07/demo3图片抓取.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 8,
      "title": "XPath 与批量采集",
      "topics": "XPath、批量下载、数据提取",
      "category": "数据采集",
      "summary": "把单次采集扩展为多页面处理。",
      "sources": [
        "examples/day08/demo1xpath学习.py",
        "examples/day08/demo2壁纸批量爬取.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 9,
      "title": "多章节文本采集",
      "topics": "数据解析、章节整理、文件写入",
      "category": "数据采集",
      "summary": "学习结构化保存多章节文本。",
      "sources": [
        "examples/day09/demo2相关知识.py",
        "examples/day09/demo3小说多章提取.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 10,
      "title": "动态接口与音乐数据",
      "topics": "接口响应、JSON、数据提取",
      "category": "数据采集",
      "summary": "从页面资源转向接口数据。",
      "sources": [
        "examples/day10/demo3字典取值.py",
        "examples/day10/音乐播放器0.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 11,
      "title": "POST 与字符串解析",
      "topics": "POST 请求、参数、解析",
      "category": "数据采集",
      "summary": "理解不同请求方式的参数组织。",
      "sources": [
        "examples/day11/demo2字符串解析.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 12,
      "title": "视频平台请求分析",
      "topics": "请求分析、批量处理、GUI 示例",
      "category": "数据采集",
      "summary": "学习请求链路与工具界面的关联。",
      "sources": [
        "examples/day12/demo3相关知识.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 13,
      "title": "浏览器自动化脚本",
      "topics": "DrissionPage、图片批量处理",
      "category": "自动化",
      "summary": "利用浏览器操作处理动态内容。",
      "sources": [
        "examples/day13/demo1百度图片自动化批量下载.py",
        "examples/day13/demo2批量自动化下载.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 14,
      "title": "社交内容与投放分析",
      "topics": "内容提取、CSV、数据整理",
      "category": "自动化",
      "summary": "将抓取记录组织为可分析表格。",
      "sources": [
        "examples/day14/demo3csv认识.py",
        "examples/day14/demo4代码错误解释.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 15,
      "title": "自由职业需求数据分析",
      "topics": "关键词采集、多页筛选、CSV",
      "category": "数据分析",
      "summary": "围绕真实业务问题整理采集流程。",
      "sources": [
        "examples/day15/demo1一个关键词数据获取.py",
        "examples/day15/demo3猿急送数据获取.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 16,
      "title": "Cookie 与价格监控",
      "topics": "会话机制、任务调度、阈值监控",
      "category": "自动化",
      "summary": "学习监控流程与登录态管理。",
      "sources": [
        "examples/day16/demo2Drissionpage爬取数据展示.py",
        "examples/day16/timing.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 17,
      "title": "验证码与多线程概念",
      "topics": "图像识别、线程、请求协作",
      "category": "自动化",
      "summary": "了解动态验证与并发的技术边界。",
      "sources": [
        "examples/day17/demo4单线程和多线程.py",
        "examples/day17/demo5多线程请求.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 18,
      "title": "闲鱼商品数据与请求分析",
      "topics": "请求参数、JSONPath、价格字段",
      "category": "数据采集",
      "summary": "分析商品数据结构与变化。",
      "sources": [
        "examples/day18/demo02jsonpath的使用.py",
        "examples/day18/demo3Drissionpage监控闲鱼数据.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 19,
      "title": "考研院校数据整理",
      "topics": "数据清洗、指标比较、分析报告",
      "category": "数据分析",
      "summary": "从分散记录生成可比较的信息。",
      "sources": [
        "examples/day19/demo1各院校历年数据采集.py",
        "examples/day19/绘制图表.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 20,
      "title": "Pyecharts 数据可视化",
      "topics": "Pandas、图表、HTML 输出",
      "category": "数据分析",
      "summary": "把清洗后的数据转化为可浏览图表。",
      "sources": [
        "examples/day20/demo02数据处理.py",
        "examples/day20/demo03可视化绘图.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 21,
      "title": "职业方向与薪资可视化",
      "topics": "模拟样本、数据大屏、图表",
      "category": "数据分析",
      "summary": "理解模拟数据分析与可视化表达。",
      "sources": [],
      "kind": "课堂代码"
    },
    {
      "day": 22,
      "title": "贝壳二手房采集案例",
      "topics": "多页采集、数据整理、Excel",
      "category": "数据采集",
      "summary": "整合网站采集、结构化字段与成果交付。",
      "sources": [
        "examples/day22/demo1贝壳二手房数据获取.py",
        "examples/day22/demo4多页数据获取.py"
      ],
      "kind": "课堂代码"
    },
    {
      "day": 23,
      "title": "Git / Gitee 与项目归档",
      "topics": "版本控制、仓库、学习成果发布",
      "category": "项目交付",
      "summary": "将分散脚本整理成可持续维护的代码记录。",
      "sources": [],
      "kind": "课程记录"
    },
    {
      "day": 24,
      "title": "GitHub Pages 与结课作品集",
      "topics": "公开站点、简历表达、AI辅助工作流",
      "category": "项目交付",
      "summary": "从课堂练习走向完整的公开展示。",
      "sources": [
        "examples/day24/桌面悬浮时钟(1).py",
        "examples/day24/简易截图工具(1).py",
        "examples/day24/高颜值桌面计算器(1).py",
        "examples/day24/便签文件(1).py",
        "examples/day24/倒计时小工具(1).py",
        "examples/day24/六合一工具中心(1).py",
        "examples/day24/六合一工具集成(1).py",
        "examples/day24/学习作息计时器(1).py",
        "examples/day24/桌面便签备忘录(1).py",
        "examples/day24/桌面便签更新(1).py"
      ],
      "kind": "课程练习文件"
    }
  ]
};
