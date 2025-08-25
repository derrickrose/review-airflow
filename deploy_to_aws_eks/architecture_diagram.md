flowchart LR
  %% === Sources / Repos ===
  subgraph GitHub["GitHub"]
    direction TB
    gh_app[App Repo<br/>(Code, Dockerfile, DAG1, DAG2)]
    gh_ops[Ops Repo<br/>(k8s: Namespace, Deployment, Ingress)]
  end

  %% === CI/CD ===
  gh_app -->|webhook| cp[AWS CodePipeline]
  cp --> cb[AWS CodeBuild]
  cb --> ecr[ECR<br/>(Container Images)]

  %% === GitOps Controller ===
  gh_ops -. watches .-> flux[FluxCD (Weave GitOps)]
  ecr -->|image tags| flux
  flux -->|apply manifests| k8s[EKS Cluster]

  %% === Networking ===
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
  alb:::edge

  classDef edge stroke-dasharray: 0;

  %% Legend (optional)
  subgraph Legend
    L1[CI/CD Push] --> L2[Container Registry]
    L3[GitOps Pull] --> L4[Kubernetes Apply]
  end
