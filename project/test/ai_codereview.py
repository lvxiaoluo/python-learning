import requests
import json
import time

# 配置基础 URL 和 PRIVATE-TOKEN
BASE_URL = "giturl"
PRIVATE_TOKEN = ""

# 设置请求头
headers = {
    "PRIVATE-TOKEN": PRIVATE_TOKEN,
    "Content-Type": "application/json"
}

# 1. 调用接口1：获取项目信息
def get_project_info(project_name):
    url = f"{BASE_URL}/projects"
    params = {
        "simple": "true",
        "search": project_name
    }
    print(f"接口1调用参数: {params}")
    response = requests.get(url, headers=headers, params=params)
    print(f"接口1调用结果: {response.text}")
    if response.status_code == 200:
        projects = response.json()
        # 精确匹配逻辑
        matched_projects = [
            p for p in projects
            if p.get("name") == project_name or p.get("name_with_namespace").endswith(f"/{project_name}")
        ]
        if len(matched_projects) == 1:
            print(f"找到唯一匹配项目: {matched_projects[0]['name_with_namespace']}")
            return matched_projects[0]  # 返回唯一匹配的项目
        elif len(matched_projects) > 1:
            raise Exception(f"找到多个匹配项目: {[p['name_with_namespace'] for p in matched_projects]}")
        else:
            raise Exception("未找到完全匹配的项目")
    else:
        raise Exception(f"接口1调用失败，状态码: {response.status_code}, 响应: {response.text}")

# 2. 调用接口2：创建项目访问令牌
def create_access_token(project_id):
    url = f"{BASE_URL}/projects/{project_id}/access_tokens"
    data = {
        "name": "AI_CodeReview",
        "scopes": ["api", "read_api", "ai_features"],
        "description": "AI代码审查",
        "expires_at": "2027-02-03",
        "access_level": 20
    }
    print(f"接口2调用参数: {data}")
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(f"接口2调用结果: {response.text}")
    if response.status_code == 201:
        return response.json()  # 返回创建的访问令牌信息
    else:
        raise Exception(f"接口2调用失败，状态码: {response.status_code}, 响应: {response.text}")

# 3. 调用接口3：创建 Webhook
def create_webhook(project_id, token):
    url = f"{BASE_URL}/projects/{project_id}/hooks"
    data = {
        "name": "AI_CodeReview",
        "description": "AI代码审查",
        "url": "aicodereviewurl",
        "token": token,
        "custom_headers": [
            {"key": "X-Custom-Programminglanguage", "value": "JAVA"},
            {"key": "X-Custom-Batchreviewsummary", "value": "TRUE"},
            {"key": "X-Custom-Filesperreview", "value": "5"},
            {"key": "X-Custom-Reviewmaxtokens", "value": "10000"}
        ],
        "push_events": True,
        "merge_requests_events": True,
        "branch_filter_strategy": "all_branches",
        "enable_ssl_verification": 1
    }
    print(f"接口3调用参数: {data}")
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(f"接口3调用结果: {response.text}")
    if response.status_code == 201:
        return response.json()  # 返回创建的 Webhook 信息
    else:
        raise Exception(f"接口3调用失败，状态码: {response.status_code}, 响应: {response.text}")

# 主流程
if __name__ == "__main__":

        # 定义项目名称列表
        project_names = [
                         ]
        for project_name in project_names:
            try:
                # 步骤1：获取项目ID
                project = get_project_info(project_name)
                project_id = project["id"]
                print(f"项目ID: {project_id}")
                time.sleep(1)  # 休眠1秒

                # 步骤2：创建访问令牌
                access_token_info = create_access_token(project_id)
                token = access_token_info["token"]
                print(f"访问令牌: {token}")
                time.sleep(1)  # 休眠1秒

                # 步骤3：创建Webhook
                webhook_info = create_webhook(project_id, token)
                print(f"Webhook创建成功: {webhook_info}")
                time.sleep(1)  # 休眠1秒
            except Exception as e:
                print(f"执行出错: {e}")

