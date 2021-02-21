class Solution:
    def interpret(self, command: str) -> str:
        parser = {
            "()": "o",
            "(al)": "al"
        }
        
        for i, j in parser.items():
            command = command.replace(i, j)
            
        return command