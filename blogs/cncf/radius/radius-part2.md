# Getting started with Radius: Run your first app

This guide will show you how to quickly get started with Radius. You’ll walk through both installing Radius and running your first Radius app.


![First Application](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hnyjutcbda46vb7mlb2j.png)

Here we have a basic container which consist of our application and a Redis as Database . 

<u>**1. Have your Kubernetes cluster handy**</u>

_If you don’t have a preferred way to create Kubernetes clusters, you could try using [k3d](https://k3d.io/), which runs a minimal Kubernetes distribution in Docker._

Ensure your cluster is set as your current context:

```
kubectl config current-context
```

<u>**2. Install Radius CLI**</u>

For installation of radius cli , you can check the previous post for details about radius cli and installation.

[Installation of Radius CLI](https://dev.to/kumail1232/radius-a-new-open-source-application-platform-for-cloud-native-apps-by-microsoft-143)

<u>**3. Initialize Radius**</u>

Create a new directory for your app and navigate into it:

```
mkdir first-app
cd first-app
```
Initialize Radius. For this example, accept all the default options (press ENTER to confirm):

```
rad init
```
Example output:

```
Initializing Radius...

✅ Install Radius v0.29
    - Kubernetes cluster: k3d-k3s-default
    - Kubernetes namespace: radius-system
✅ Create new environment default
    - Kubernetes namespace: default
    - Recipe pack: local-dev
✅ Scaffold application docs
✅ Update local configuration
```
**Initialization complete! Have a RAD time 😎**

In addition to starting Radius services in your Kubernetes cluster, this initialization command creates a default application (app.bicep) as your starting point. It contains a single container definition (demo).

```
// Import the set of Radius resources (Applications.*) into Bicep
import radius as radius

@description('The app ID of your Radius Application. Set automatically by the rad CLI.')
param application string

resource demo 'Applications.Core/containers@2023-10-01-preview' = {
  name: 'demo'
  properties: {
    application: application
    container: {
      image: 'ghcr.io/radius-project/samples/demo:latest'
      ports: {
        web: {
          containerPort: 3000
        }
      }
    }
  }
}
```

This file will run the `ghcr.io/radius-project/samples/demo:latest` image. This image is published by the Radius team to a public registry, you do not need to create it.

<u>**4. Run the app**</u>

Use the below command to run the app in your environment, then access the application by opening [http://localhost:3000](http://localhost:3000) in a browser.

```
rad run app.bicep
```
This command:

1. Runs the application in your Kubernetes cluster
2. Creates a port-forward from localhost to port 3000 inside the container so you can navigate to the app’s frontend UI
3. Streams container logs to your terminal

In your browser you should see the demo app:

![Demo App](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7nkc74nbu4vxf5v37n07.png)

Congrats! You’re running your first Radius app. When you’re ready to move on to the next step, use `CTRL+ C` to exit the command.

<u>**5. Add Database**</u>

This step will add a database (Redis Cache) to the application.

You can create a Redis Cache using Recipes provided by Radius. The Radius community provides Recipes for running commonly used application dependencies, including Redis.

In this step you will:

Add Redis to the application using a [Recipe](https://docs.radapp.io/guides/recipes/overview/).
Connect to Redis from the `demo` container using environment variables that Radius automatically sets.

Open `app.bicep` in your editor and get ready to edit the file.

First add some new code to `app.bicep` by pasting in the content below at the end of the file. 
This code creates a Redis Cache using a Radius Recipe:

```
@description('The environment ID of your Radius Application. Set automatically by the rad CLI.')
param environment string

resource db 'Applications.Datastores/redisCaches@2023-10-01-preview' = {
  name: 'db'
  properties: {
    application: application
    environment: environment
  }
}

```
Next, update your container definition to include `connections` inside `properties`. This code creates a connection between the container and the database. Based on this connection, Radius will inject [environment variables](https://docs.radapp.io/guides/author-apps/containers/overview/#connections) into the container that inform the container how to connect. You will view these in the next step.

```
resource demo 'Applications.Core/containers@2023-10-01-preview' = {
  name: 'demo'
  properties: {
    application: application
    container: {
      image: 'ghcr.io/radius-project/samples/demo:latest'
      ports: {
        web: {
          containerPort: 3000
        }
      }
    }
    connections: {
      redis: {
        source: db.id
      }
    }
  }
}
```
**NOTE:-** Check the connection block in the above code block ,we will provide the redis connection with the demo application 

our updated `app.bicep` will look like this:

```
// Import the set of Radius resources (Applications.*) into Bicep
import radius as radius

@description('The app ID of your Radius Application. Set automatically by the rad CLI.')
param application string

resource demo 'Applications.Core/containers@2023-10-01-preview' = {
  name: 'demo'
  properties: {
    application: application
    container: {
      image: 'ghcr.io/radius-project/samples/demo:latest'
      ports: {
        web: {
          containerPort: 3000
        }
      }
    }
    connections: {
      redis: {
        source: db.id
      }
    }
  }
}

param environment string
resource db 'Applications.Datastores/redisCaches@2023-10-01-preview' = {
  name: 'db'
  properties: {
    application: application
    environment: environment
  }
}
```

<u>**6. Rerun the application with a database**</u>

Use the command below to run the updated application again, then open the browser to [http://localhost:3000](http://localhost:3000).

```
rad run app.bicep
```


![Demo App with Redis DB](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wrd7p6slkbn9l7wdnkyz.png)

Navigate to the Todo List tab and test out the application. Using the Todo page will update the saved state in Redis:

Press `CTRL+ C` when you are finished with the website.


<u>**7. View the application connections**</u>

Radius Connections are more than just environment variables and configuration. You can also access the “application graph” and understand the connections within your application with the following command:

```
rad app connections
```
You should see the following output, detailing the connections between the `demo` container and the `db` Redis Cache, along with information about the underlying Kubernetes resources running the app:

```
Displaying application: demo

Name: demo (Applications.Core/containers)
Connections:
  demo -> db (Applications.Datastores/redisCaches)
Resources:
  demo (kubernetes: apps/Deployment)
  demo (kubernetes: core/Secret)
  demo (kubernetes: core/Service)
  demo (kubernetes: core/ServiceAccount)
  demo (kubernetes: rbac.authorization.k8s.io/Role)
  demo (kubernetes: rbac.authorization.k8s.io/RoleBinding)

Name: db (Applications.Datastores/redisCaches)
Connections:
  demo (Applications.Core/containers) -> db
Resources:
  redis-r5tcrra3d7uh6 (kubernetes: apps/Deployment)
  redis-r5tcrra3d7uh6 (kubernetes: core/Service)
```
So, we have Completed Building our First Application on Radius Successfully 

if you have any comments or questions feel free to drop down below . 

Thank You 



