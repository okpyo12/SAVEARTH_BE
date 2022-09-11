from .models import Trash
from .serializers import TrashSerializer
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class TrashViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Trash.objects.all()
    serializer_class = TrashSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id','trash_x','trash_y']

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)