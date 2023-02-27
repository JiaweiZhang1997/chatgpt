from vedio import Monitor
from asr import vedio_to_text, main_dir
from tts import text_to_vedio, get_xml
import Play_mp3
from chatgpt import start_chatgpt, chatgpt
# 选择语音识别（语音） or 输入文本（文本）
mode = "文本"

if __name__ == "__main__":
    chatbot, conversation_id, parent_id, prev_text = start_chatgpt()

    # 如果chatbot初始化成功，则继续
    if prev_text != "":

        # 循环
        while True:
            if mode == "语音":
                # 录音
                Monitor()
                # # 语音转文字
                sentence = vedio_to_text()
            elif mode == "文本":
                sentence = input("我：")
            # 获取chatgpt的回答
            try:
                # answer = chatgpt(chatbot=chatbot, text=sentence, conversation_id=conversation_id, parent_id=parent_id)
                answer = chatgpt(chatbot=chatbot, text=sentence, conversation_id=conversation_id)
            except:
                answer = "请求异常！"
            # 创建xml配置文件
            print(answer)
            get_xml(text = answer)
            # 文字转语音
            text_to_vedio(main_dir + r"\SSML.xml", main_dir + r"\output")
            # 播放语音
            Play_mp3.play(main_dir + r"\output.mp3")