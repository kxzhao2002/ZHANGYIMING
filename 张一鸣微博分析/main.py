import openai
import PyPDF2

# 设置OpenAI API密钥
openai.api_key = 'API_Key'


# 读取PDF文件内容的函数
def read_pdf_content(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        content = ""
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            content += page.extract_text()
        return content


# 调用OpenAI API进行文本分析
def analyze_text(text):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=text,
        max_tokens=100
    )
    return response.choices[0].text.strip()


# 读取PDF文件内容
pdf_content = read_pdf_content('张一鸣微博创业思考231条精华版.pdf')

# 提出问题并调用API进行回答
question_1 = "作者的内容截止到2016年，请根据你的理解，推测在2023年，作者的公司可能在从事的业务、发展情况等。"
answer_1 = analyze_text(question_1 + pdf_content)

question_2 = "以下哪一条更可能是作者所创办公司的使命？请简述原因：1）激发创造，丰富生活；2）用科技让复杂的世界更简单；3）帮大家吃得更好，生活更好；4）让全球多一点幸福。"
answer_2 = analyze_text(question_2 + pdf_content)

question_3 = "请尝试用MBTI人格分析法来分析作者的人格，并给出较详细的理由。"
answer_3 = analyze_text(question_3 + pdf_content)

question_4 = "这条内容表达作者什么思考？"
answer_4 = analyze_text(question_4 + pdf_content)

question_5 = "你觉得作者可能是中国哪一位著名互联网企业家很类似？简述理由。"
answer_5 = analyze_text(question_5 + pdf_content)

question_6 = "推测以下信息并简单说明原因：1）作者的大概年龄；2）作者的公司可能的管理方式和企业文化；3）作者比较推崇哪些公司，比较反感那些公司。"
answer_6 = analyze_text(question_6 + pdf_content)

question_7 = "如果作者的公司开展国际化业务，你认为最可能直接竞争的美国公司有哪些？为什么？"
answer_7 = analyze_text(question_7 + pdf_content)

question_8 = "你觉得作者创办的公司在美国经营时，有哪些尤其要注意的地方？可能引起哪些争议？"
answer_8 = analyze_text(question_8 + pdf_content)

question_9 = "你觉得作者可能是中国哪一位著名互联网企业家？简述理由。"
answer_9 = analyze_text(question_9 + pdf_content)

print("问题1：")
print(answer_1)
print("问题2：")
print(answer_2)
print("问题3：")
print(answer_3)
print("问题4：")
print(answer_4)
print("问题5：")
print(answer_5)
print("问题6：")
print(answer_6)
print("问题7：")
print(answer_7)
print("问题8：")
print(answer_8)
print("问题9：")
print(answer_9)
