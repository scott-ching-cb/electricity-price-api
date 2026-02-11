# Electricity Price API Challenge

For the 'Electricity Price API Challenge', Python and Flask were selected for development purposes given that the role
will be utilizing this tech stack. The application is structure using an n-layered architecture which provides scalability
as the application increases in size and domain(s).

This layered architecture consists of:
- infrastructure layer: containing required middleware, layer set-up (e.g. models and converters), logs, and potential future database and ORM setup.
- presentation layer: contains the main routing logic enabling a quicker look-up into the application code.
- application layer: separated package namespaces for different domains, each with their own required definitions (e.g. exceptions) and called by the 'presentation' layer. The usecases represent the typical 'service' layer which interacts with DTOs and can make requests to access data.
- repository layer: contains 'gateways' which implement application-domain interfaces to access data (currently only CSV)

## Assumptions
The following assumptions were made whilst planning and implementing this challenge:
- Logging, monitoring and observability are out-of-scope but can be easily implemented if required in the infrastructure middleware layer.
- The 'state' argument which is to be received will be a <b>path parameter</b> in a <b>GET request</b> given that it is a request to access a resource.
  - This can be further re-structured (out-of-scope), based on URI, for more actions by utilizing query parameters. An example of this is '/price/average?state=Vic' which enables extension of the primary path.
- Development would occur within a containerized environment (assumed out-of-scope but happy to complete if required) thereby simulating a production-like environment and reducing application variability (e.g. instructions required to execute program).
- Flask's default WSGI would be replaced by a production-ready WSGI (e.g. Waitress).

## Instructions for Starting the Flask Application
1. Ensure that `python3` is installed (should come with `pip` installed).
2. Navigate to the project root directory and execute `pip install` to ensure all project dependencies are downloaded.
3. Ensure that `flask` is installed as described [here](https://flask.palletsprojects.com/en/stable/installation/)
4. From the `/electricity-price-api` directory, navigate to the 'app' package and execute the following command: `flask --app __main__ run`


## Instructions for Running Unit Testcases
1. Navigate to the root electricity-price-api directory.
2. Ensure that python version 3.x is installed as well as the `unittest` dependency (via pip).
3. Execute the following command `python3 -m unittest`.
