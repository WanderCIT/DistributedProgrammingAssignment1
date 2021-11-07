import grpc
from concurrent import futures
import time
import spelling_pb2_grpc as pb2_grpc
import spelling_pb2 as pb2


class SpellingBeeService(pb2_grpc.SpellingBeeServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        word = request.word
        result = f'Hello I am up and running received "{word}" message from you'
        response = 'sucess'
        result = {'word': result, 'response': response}

        return pb2.SpellingBeeWordResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_SpellingBeeServicer_to_server(SpellingBeeService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()