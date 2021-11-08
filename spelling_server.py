import grpc
from concurrent import futures
import time
import spelling_pb2_grpc as pb2_grpc
import spelling_pb2 as pb2
from random import randint


class SpellingBeeService(pb2_grpc.SpellingBeeServicer):

    def __init__(self, *args, **kwargs):
        pass


    ## Taking your code as a reference get a random pangram
    def pangram_for_letter_list(self, word_in):
        if len(set(word_in)) == 8 and 's' not in word_in:
            return True
        else:
            return False

    # Generate set of characters
    def generate_letter_list(self):
        pangrams = []
        letters = []
        with open("dictionary.txt") as dictionary:
            for word in dictionary:
                if (self.pangram_for_letter_list(word)):
                    pangrams.append(word)

        rand_num = randint(0, len(pangrams))
        random_pangram = pangrams[rand_num]
        for letter in set(random_pangram):
            if letter != '\n':
                letters.append(letter)

        # Keeping the debug for cheating purposes
        print(f'PANGRAM => {random_pangram}')
        print(f'FINAL LETTERS => {letters}')

        return letters

        

    def GetLetters(self, request, context):
        
        # Generate a set of characters and return them to the client
        letters = self.generate_letter_list()

        return pb2.SpellingLetters(letters=letters)

    # Check if word is a pangram (to my understanding)
    def is_panagram(self, word, letters):

        for letter in letters:
            print(f'Letter => ', letter.lower())
            if (letter.lower() not in word):
                return False
        
        return True


    def CheckWord(self, request, context):

        # get the data from the incoming request
        word = request.word.lower()
        letters = request.letters
        score = request.score
        exists = False
        points = 0

        # Check if word exists
        with open('dictionary.txt') as file:
            contents = file.read()
            if word in contents:
                exists = True

        # Check if word respects the rules of the game and return the result + score
        if (len(word)>3 and (letters[0].lower() in word) and exists):
            for letter in word:
                if letter.lower() in letters:
                    pass
                else:
                    result = {
                        'word': word,
                        'valid': "Invalid word",
                        'reason': "Used invalid letters",
                        'score': score
                    }
                    return pb2.SpellingBeeWordResponse(**result)
            if (len(word) < 5):
                points = 1
            elif (self.is_panagram(word.lower(), letters)):
                points = len(word) + 7
            else:
                points = len(word)

            is_panagram = self.is_panagram(word.lower(), letters)

            result = {
                'word': word,
                'valid': "Valid word",
                'reason': "Respects all rules",
                'score':score+points
            }
            return pb2.SpellingBeeWordResponse(**result)
        else:
            result = {
                'word': word,
                'valid': "Invalid word",
                'reason': "Word too short or didn't use centre letter",
                'score': score
            }
            return pb2.SpellingBeeWordResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_SpellingBeeServicer_to_server(SpellingBeeService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()