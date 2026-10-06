# estudo_argo

1- Ter o docker, kind e kubectl instalados.

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

Em seguida, abra o navegador e acesse `https://localhost:8080`. O login padrão é `admin` e a senha é o nome do pod do servidor Argo CD:

```bash
kubectl get pods -n argocd -l app.kubernetes.io/name=argocd-server -o name | cut -d'/' -f 2
```