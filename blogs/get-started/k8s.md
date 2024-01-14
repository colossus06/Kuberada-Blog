# Kubernetes


🚀 **Getting Started with Kubernetes: Your Favorite Environments Guide**

So, you're ready to dive into the world of Kubernetes but unsure where to start? Fear not! We've got you covered with a beginner-friendly guide using our favorite environments – Minikube, k3d, and Vagrant. Whether you prefer to keep it local or venture into the cloud with a Codespace environment, we've got options for everyone.

### 1. **Minikube: Quick and Simple**

Minikube is your go-to if you're looking for a hassle-free Kubernetes setup on your local machine. Here's a quick start:

```bash
# Install Minikube (if not already installed)
brew install minikube

# Start Minikube cluster
minikube start

# Verify your setup
kubectl get nodes
```

Now, you have a single-node Kubernetes cluster ready for exploration. Perfect for testing and learning the basics.

### 2. **k3d: Lightweight and Portable**

If you're a fan of lightweight environments, k3d is your companion. It spins up a Kubernetes cluster in Docker containers, making it easy to set up and tear down:

```bash
# Install k3d (if not already installed)
brew install k3d

# Create k3d cluster
k3d cluster create <yourk3dcluster>

# Verify your setup
kubectl get nodes
```

Enjoy the simplicity of k3d, which provides a fast and lightweight Kubernetes environment for your experiments.

### 3. **Vagrant: Customizable Kubernetes Playground**

**3-node**

For those who prefer a more customizable setup, Vagrant is the way to go. You can choose between a 3-node or 6-node local setup for a more realistic cluster experience:

We have setup a 3 node cluster for simple three tier applications and development purposes.
Check Kuberada labs repo for 3-node cluster Vagrantfile setup [here](https://github.com/kuberada/kuberada-labs/tree/main/getting-started/k8s/3-node).

```bash
# Install Vagrant (if not already installed)
brew install vagrant

# Choose your setup
# 3-node setup
vagrant up 3-node
```

**6-node**

We have a 6 node vagrant setup for distributed applications, microservices exploration.
Check Kuberada labs repo for 6-node cluster setup [here](https://github.com/kuberada/kuberada-labs/tree/main/getting-started/k8s/6-node). 

```sh
# 6-node setup
vagrant up 6-node

# Verify your setup
kubectl get nodes
```

Vagrant allows you to experiment with different node configurations, providing a scalable environment right on your local machine.

### 4. **Codespace Environment: Cloud-Powered Learning**

Prefer to keep it cloud-native? Utilize a Codespace environment with the following specifications:

We have a kubernetes cluster created with k3d. Container runtime used by the node is containerd and the version of k8s is `v1.27` with 4 cores, 16 GB RAM, 32 GB storage.

Check Kuberada labs repo for 6-node cluster setup [here](https://github.com/kuberada/kuberada-labs/tree/main/getting-started/k8s/k3d-codespace).


Clone your Kubernetes project into the Codespace and run:

```bash
# Set up your Kubernetes environment
kubectl get nodes
```

Now you have a cloud-powered Kubernetes environment right at your fingertips.

### Conclusion:

Whether you're a fan of Minikube, k3d, Vagrant, or Codespaces, we've got a Kubernetes environment tailored to your preferences. Choose the setup that suits your learning style, experiment with basic Kubernetes commands, and get ready to unlock the full potential of container orchestration.

Happy Kuberneting! 🌐🚀

