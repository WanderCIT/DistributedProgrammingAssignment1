import grpc
from concurrent import futures
import time
import spelling_pb2_grpc as pb2_grpc
import spelling_pb2 as pb2


class SpellingBeeService(pb2_grpc.SpellingBeeServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetLetters(self, request, context):
        letters = {
            'letter1': 'A',
            'letter2': 'B',
            'letter3': 'C',
            'mainLetter': 'X',
            'letter4': 'D',
            'letter5': 'E',
            'letter6': 'F',
        }

        # letter = {'letter': 'A'}

        return pb2.SpellingLetters(**letters)

    def valid_word(self, word, letters):
        print("VALID WORD CALLED")
        if (len(word)>3 and (letters[0] in word)):
            for letter in word:
                if letter in letters:
                    pass
                else:
                    return False
            return True
        else:
            return False


    def CheckWord(self, request, context):

        # get the string from the incoming request
        word = request.word.lower()
        letters = request.letters
        exists = False

        with open('dictionary.txt') as file:
            contents = file.read()
            if word in contents:
                exists = True

        print(f"EXISTS => {exists}")
        print(f"LENGTH => {len(word)}")
        print(f"LETTERS IN => {letters[0]}")

        if (len(word)>3 and (letters[0].lower() in word) and exists):
            print("DEBUG 1")
            for letter in word:
                if letter.upper() in letters:
                    pass
                else:
                    print("DEBUG 2")
                    result = {'word': word, 'valid': "Invalid word", 'reason': "Used invalid letters"}
                    return pb2.SpellingBeeWordResponse(**result)
            print("DEBUG 3")
            result = {'word': word, 'valid': "Valid word", 'reason': "Respects all rules"}
            return pb2.SpellingBeeWordResponse(**result)
        else:
            print("DEBUG 4")
            result = {'word': word, 'valid': "Invalid word", 'reason': "Word too short or didn't use centre letter"}
            return pb2.SpellingBeeWordResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_SpellingBeeServicer_to_server(SpellingBeeService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()