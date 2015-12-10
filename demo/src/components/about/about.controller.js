class AboutController {

  constructor(aboutService) {
    this.name = 'Contact Us'
    this.model = {};
    this.schema = {
      type: "object",
      properties: {
        name: { type: "string", minLength: 2, title: "Name", description: "Name or alias" },
        title: {
          type: "string",
          enum: ['dr','jr','sir','mrs','mr','NaN','dj']
        }
      },
      "required": [
        "name",
      ]
    };
    this.form = [
      "*",
      {
        type: "submit",
        title: "Save"
      }
    ];
    this.result = {};
    this.service = aboutService;
  }

  getSchema() {
    this.service.getSchema().then((res) => {
      this.result = res.data;
      console.log(this.result);
      this.schema = res.data;
      this.form = res.data.form;
      alert('getSchema');
    });
  }

  onSubmit(form) {
    // First we broadcast an event so all fields validate themselves
    $scope.$broadcast('schemaFormValidate');

    // Then we check if the form is valid
    if (form.$valid) {
      console.log('form is valid')
    } else {
      console.log('form is invalid')
    }
  }
}

export default AboutController;
