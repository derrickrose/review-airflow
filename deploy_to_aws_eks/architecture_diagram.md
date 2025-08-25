```mermaid
flowchart LR
  subgraph GitHub["GitHub"]
    direction TB
    gh_app[App Repo\n(Code, Dockerfile, DAG1, DAG2)]
    gh_ops[Ops Repo\n(k8s: Namespace, Deployment, Ingress)]
  end

  gh_app -->|webhook| cp[AWS CodePipeline]
  cp --> cb[AWS CodeBuild]
  cb --> ecr[ECR\n(Container Images)]

  gh_ops -.->|watches| flux[FluxCD (Weave GitOps)]
  ecr -->|image tags| flux
  flux -->|apply manifests| k8s[EKS Cluster]

  subgraph VPC["AWS VPC (3 AZs)"]
    direction LR
    subgraph AZA["AZ A (Private + Public)"]
      nodeA[(EKS Node)]
    end
    subgraph AZB["AZ B (Private + Public)"]
      nodeB[(EKS Node)]
    end
    subgraph AZC["AZ C (Private + Public)"]
      nodeC[(EKS Node)]
    end
  end

  k8s --- nodeA
  k8s --- nodeB
  k8s --- nodeC

  flux --> ns[Namespace]
  flux --> dep[Deployment/Service]
  dep -->|expose| alb[Application Load Balancer (Ingress)]

  subgraph Legend
    L1[CI/CD Push] --> L2[Container Registry]
    L3[GitOps Pull] --> L4[Kubernetes Apply]
  end
```