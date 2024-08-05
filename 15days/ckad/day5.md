(day5)=
# 🎯  Day 5: Application Deployment - The Art of Seamless Rollouts

Welcome back, aspiring CKADs! Today, we delve into the second core domain of the exam: Application Deployment. This domain makes up a significant 20% of the test, so it's crucial to master the art of deploying applications smoothly and efficiently within Kubernetes.

While we can't cover every nuance in a single day, we'll build a solid foundation and equip you with the key strategies and techniques to tackle deployment challenges head-on. 

## 🚀  Key Concepts: Your Deployment Toolkit

* **Deployments:**  These are your workhorses for managing stateless applications.  You'll need to be comfortable creating, updating, and scaling deployments.
* **Rollouts:**  Understand the different rollout strategies (RollingUpdate, Recreate) and how to control the deployment process.
* **Rollbacks:**  Know how to roll back a deployment if something goes wrong.
* **ReplicaSets:**  Understand how ReplicaSets work behind the scenes to maintain the desired state of your deployments.
* **Probes:**  Use liveness and readiness probes to ensure your applications are healthy and ready to serve traffic.

## 🛠️  Key Skills for Day 5:

* **Creating and managing deployments:** Use `kubectl` to create, update, and scale deployments.
* **Configuring rollout strategies:** Understand how to configure `maxUnavailable` and `maxSurge` to control the rollout process.
* **Performing rollbacks:** Use `kubectl rollout undo` to revert to a previous version of a deployment.
* **Configuring liveness and readiness probes:** Use probes to ensure your applications are healthy and ready to serve traffic.

## 📚 Essential Resources:

* **Kubernetes Documentation - Deployments:** [https://kubernetes.io/docs/concepts/workloads/controllers/deployment/](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
* **Kubernetes Documentation - ReplicaSets:** [https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
* **Kubernetes Documentation - Probes:** [https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)

## 💡  Pro Tips:

* **Practice, Practice, Practice:** Create and manage deployments in your local Kubernetes cluster. Experiment with different rollout strategies and probes.
* **Understand the Tradeoffs:**  Each rollout strategy has its advantages and disadvantages. Choose the right strategy for your application and its requirements.
* **Automate:**  Consider using tools like Helm or Kustomize to streamline your deployment process.
* **Monitor:**  Use monitoring tools to track the health and performance of your deployments.

## 🏋️‍♀️ Today's Action:

1. **Deep Dive into the Docs:**  Explore the Kubernetes documentation on the topics listed above. Pay close attention to the practical examples and use cases.
2. **Hands-On Labs:**  Complete labs that focus on creating, updating, scaling, and rolling back deployments.  Practice configuring liveness and readiness probes.
3. **Share Your Progress:**  Post a summary of your key learnings or any challenges you encountered on social media using the hashtag `#CKADSprint`.

Remember, mastering application deployment is essential for success on the CKAD exam. Let's continue building your Kubernetes skills and confidence! 

**Up next on Day 6:** We'll explore Application Observability and Maintenance – keeping your applications running smoothly and troubleshooting issues like a pro. Get ready to dive in! 

**CKAD Sprint: 5 Days In - Where We Stand and Where We're Going**

We've covered a lot of ground in the first 5 days of our CKAD sprint!

✅  **Day 1: Orientation and Mindset** - We laid the groundwork for success, understanding the exam format, setting the right mindset, and gathering essential resources.

✅  **Day 2: Exam Logistics and Tech Readiness** -  We tackled the practical aspects of the exam, ensuring a smooth and stress-free experience on test day.

✅  **Day 3: Time Management and Exam Strategy** - We explored key strategies for prioritizing tasks, managing time effectively, and approaching the exam with confidence. 

✅  **Day 4: Application Design and Build** -  We delved into the first core domain of the exam, mastering the building blocks of Kubernetes applications and designing for scalability and resilience.

✅  **Day 5: Application Deployment** - We explored the art of seamless rollouts, focusing on deployments, rollbacks, and ensuring application health with probes.

**Where We're Headed:** 

Next, we'll tackle **Application Observability and Maintenance** and **Application Environment, Configuration, and Security**. We'll equip you with the skills to monitor, troubleshoot, and secure your Kubernetes applications, rounding out your CKAD expertise. 

Keep up the momentum!

*You can track your progress with [CKAD Sprint Tracker](#tracker).*

