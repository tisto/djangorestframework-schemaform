class UserService {
  constructor($http) {
    this.$http = $http;
  }

  getSchema() {
    return this.$http
      .get('user')
      .then((result) => {
        console.log('getSchema');
        console.log(result);
        return result.data;
      });
  }
}

export default UserService;
