import json
import re

# ====== 简单规则模拟“代码生成” ======

def generate_code(user_input: str) -> str:
    user_input = user_input.lower()

    # 示例1：Flask 登录接口
    if "登录" in user_input or "login" in user_input:
        return """from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == '123456':
        return jsonify({'msg': 'success'})
    return jsonify({'msg': 'fail'})

if __name__ == '__main__':
    app.run(debug=True)
"""

    # 示例2：简单工具函数
    if "排序" in user_input or "sort" in user_input:
        return """def sort_list(data):
    return sorted(data)

print(sort_list([3, 1, 2]))
"""

    # 默认返回
    return "# 暂未匹配到模板，可以扩展规则或接入大模型"


# ====== 简单“任务拆解” ======

def plan_task(user_input: str):
    return [
        "分析需求",
        "匹配代码模板",
        "生成代码",
        "校验输出"
    ]


# ====== 简单校验 ======

def validate_output(code: str):
    if not code.strip():
        return "生成失败：内容为空"

    # 简单检查是否像代码
    if not re.search(r"(def |class |@app|import )", code):
        return "生成结果可能不完整，请检查输入"

    return code


# ====== Agent 主流程 ======

def run_agent(user_input: str):
    print("🔍 正在分析需求...")
    tasks = plan_task(user_input)

    print("📋 任务流程：", " -> ".join(tasks))

    print("⚙️ 正在生成代码...")
    result = generate_code(user_input)

    print("✅ 校验中...")
    final_output = validate_output(result)

    return final_output


# ====== 程序入口 ======

if __name__ == "__main__":
    print("=== AI Dev Agent（简化版）===")
    user_input = input("请输入你的需求：")

    output = run_agent(user_input)

    print("\n📦 生成结果：\n")
    print(output)