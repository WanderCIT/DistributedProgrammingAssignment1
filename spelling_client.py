import grpc
import spelling_pb2_grpc as pb2_grpc
import spelling_pb2 as pb2


class SpellingClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.SpellingBeeStub(self.channel)

    def get_url(self, word):
        """
        Client function to call the rpc for GetServerResponse
        """
        word = pb2.SpellingBeeWord(word=word)
        print(f'{word}')
        return self.stub.GetServerResponse(word)


if __name__ == '__main__':
    client = SpellingClient()
    result = client.get_url(word="Ander")
    print(f'{result}')
