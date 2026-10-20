# estudo_argo

1- Ter o docker, kind, kubectl e o argocd CLI instalados.

2- Criar um cluster com kind.
```bash
kind create cluster --name argocd-lab
```
3- Verificar se o cluster foi criado corretamente.

```bash
kubectl get nodes
```

4- Verificar os contextos do kubectl.

```bash
kubectl config get-contexts
```

5- Instalar o Argo CD no cluster.

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml --server-side
```

6- Verificar se o Argo CD foi instalado corretamente.

```bash
kubectl get pods -n argocd
```

## Acessando o Argo CD
Para acessar o Argo CD, é necessário expor o serviço `argocd-server` usando port-forwarding.

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```
Pronto, agora podemos acessar o ArgoCD através do endereço localhost:8080, tanto pelo navegador quanto pelo CLI.

Para fazer a autenticação no ArgoCD, precisamos executar o seguinte comando:

```bash
argocd login localhost:8080
```

Irá solicitar o nome de usuário e a senha. O nome de usuário padrão é `admin` e a senha pode ser obtida rodando o comando abaixo:

```bash
kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64 -d
```


## Argo Workflow

1- Criar cluster com kind (se ainda não tiver sido criado anteriormente).

```bash
kind create cluster --name argo-workflow-lab
```

2- Verificar se o cluster foi criado corretamente.

```bash
kubectl get nodes
```

3- Configurar o contexto do kubectl para o cluster do Argo Workflow.

```bash
kubectl config current-context
```

4- Instalar o Argo Workflow no cluster.

```bash
ARGO_WORKFLOWS_VERSION="v4.1.5"
kubectl create namespace argo
kubectl apply --server-side -n argo -f "https://github.com/argoproj/argo-workflows/releases/download/${ARGO_WORKFLOWS_VERSION}/quick-start-minimal.yaml"
```

5- Verificar se o Argo Workflow foi instalado corretamente.

```bash
kubectl get pods -n argo
```

6- Acessar a interface web do Argo Workflow via port-forward.

```bash
kubectl -n argo port-forward svc/argo-server 2746:2746
```
Agora podemos acessar a interface web do Argo Workflow através do endereço localhost:2746 no navegador.

### Executando um Workflow simples no Argo Workflow

```bash
kubectl create -n argo -f https://raw.githubusercontent.com/argoproj/argo-workflows/main/examples/hello-world.yaml
```

Podemos verificar o status do Workflow criado com o seguinte comando, ou pelo frontend da interface web do Argo Workflow em localhost:2746:

```bash
kubectl get workflows -n argo
```
