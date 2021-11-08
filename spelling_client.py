import grpc
import spelling_pb2_grpc as pb2_grpc
import spelling_pb2 as pb2
from simple_term_menu import TerminalMenu


class SpellingClient(object):
    """
    Client for gRPC functionality
    """

    __instance = None

    def getInstance():
        """ Static access method. """
        if SpellingClient.__instance == None:
            SpellingClient()
        return SpellingClient.__instance

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.SpellingBeeStub(self.channel)

        """ SINGLETON IMPLEMENTATION"""
        """ Virtually private constructor. """
        if SpellingClient.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            SpellingClient.__instance = self

    def check_word(self, word, letters, score):
        """
        Client function to call the rpc for GetServerResponse
        """
        request = pb2.SpellingBeeWordRequest(word=word, letters=letters, score=score)
        return self.stub.CheckWord(request)

    def get_letters(self):
        letter_request = pb2.LetterRequest()
        return self.stub.GetLetters(letter_request)


    def remind_letters(self, letters):
        print(f'Letters = {letters}')
    
    def show_menu():
        
        input1 = input()


if __name__ == '__main__':
    score = 0
    options = ["Remind Letters", "Submit Word", "Exit!"]
    terminal_menu = TerminalMenu(options)
    client = SpellingClient()
    print(f'Checking singleton implementation: SpellingClient class initialization => ', client)
    client1 = SpellingClient.getInstance()
    print(f'Checking singleton implementation: reference to previously created SpellingClient class => ', client1)
    letters_response = client.get_letters()

    print(f'Letters = {letters_response}')

    # Static letters since I cannot get the ones I get from the server into an array fortmat
    letters = ['T', 'R', 'C', 'O', 'A', 'Y', 'U']

    while True:
        menu_entry_index = terminal_menu.show()
        if (menu_entry_index == 0):
            client.remind_letters(letters_response)
        elif (menu_entry_index == 1):
            word = input("Write word")
            result = client.check_word(word=word, letters=letters, score=score)
            score = result.score
            print(f'RESULT IS => {result}')
        else:
            break
    
