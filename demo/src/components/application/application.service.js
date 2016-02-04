class ApplicationService {
  constructor($http) {
    this.$http = $http;
  }

  getSchema() {
    return this.$http
      .get('application')
      .then((result) => {
        console.log('getSchema');
        console.log(result);
        return result.data;
      });
  }
}

export default ApplicationService;
