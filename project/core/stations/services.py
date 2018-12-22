from django.db.models import Q

from stations.models import Station, Net


class StationService(object):
    def create_station(self, user, data):
        station = Station.objects.create(
                owner = user,
                name = data.get('name'),
                details = data.get('details', ''),
        )
        return station

    def get_user_stations(self, user):
        return Station.objects.filter(Q(members=user) | Q(owner=user))


#singletons
station_service = StationService()