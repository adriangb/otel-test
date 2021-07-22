# demo

Install:
- kind: https://kind.sigs.k8s.io
- helm: https://helm.sh
- kubectl: https://kubernetes.io/docs/tasks/tools/

Run `make deploy`.

Set up a port forward for the `app` pod on port 8000 using k9s or kubectl.
Naviage to `localhost:8000` to start emitting traces.

Check the logs for the `opentelemetry-collector-...` pod.
