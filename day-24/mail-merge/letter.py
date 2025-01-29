from os import path

RELATIVE_WORK_DIR_PATH = path.dirname(__file__)
TEMPLATE_LETTER_PATH = path.join(RELATIVE_WORK_DIR_PATH,"Input\Letters\\","starting_letter.txt")
RELATIVE_OUTPUT_PATH = "Output\\ReadyToSend\\"

class Letter:

    def __init__(self, name: str):
        self.name = name
        self.letter_content:list[str] = []
        self.prepare_letter()
        self.save_letter()

    def prepare_letter(self):
        with open(TEMPLATE_LETTER_PATH) as template_letter:
            self.letter_content = template_letter.readlines()
        self.letter_content[0] = self.letter_content[0].replace("[name]", self.name)

    def save_letter(self):
        with open(path.join(RELATIVE_WORK_DIR_PATH,RELATIVE_OUTPUT_PATH,f"letter_for_{self.name}.txt"),mode="w") as letter_to_send:
            letter_to_send.writelines(self.letter_content)
