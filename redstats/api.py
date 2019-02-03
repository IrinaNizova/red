from redstats.serializers import SubscribersSerializer, ImagesParamsSerializer
from redstats.models import ImagesParams, Subscribers
from rest_framework import mixins, viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.mail import send_mail
from datetime import datetime, timedelta



class SubscribersList(mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = Subscribers.objects.all()
    serializer_class = SubscribersSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ImagesParamsList(viewsets.ViewSet):

    queryset = ImagesParams.objects.all()
    serializer_class = ImagesParamsSerializer

    @action(methods=['post'], detail=False)
    def set_image(self, request):
        serializer = ImagesParamsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            subscribers = Subscribers.objects.filter(level_red__lte=request.data['percent_red'])

            send_mail('New picture', 'Picture {} with level red {} come'.format(request.data['title'], request.data['percent_red']),
                      'irinanizova0@gmail.com', [subscriber.email for subscriber in subscribers], fail_silently=False)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(methods=['get'], detail=True)
    def more_red(self, request, pk):
        images = ImagesParams.objects.filter(percent_red__gt=pk)
        serializer = ImagesParamsSerializer(images, many=True)
        return Response(serializer.data)


    @action(methods=['get'], detail=True)
    def last_days(self, request, pk):
        images = ImagesParams.objects.filter(time__gte=datetime.today()-timedelta(days=int(pk)))
        serializer = ImagesParamsSerializer(images, many=True)
        return Response(serializer.data)










