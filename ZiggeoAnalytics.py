class ZiggeoAnalytics:

    def __init__(self, application):
        self.__application = application

    def get(self, data = None):
        return self.__application.connect.postJSON('/analytics/get', data)

