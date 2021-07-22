.PHONY: run-app init cluster-up deploy cluster-down

.init:
	@deactivate > /dev/null 2>&1 || true
	pip install -U --pre poetry && poetry install
	@touch .init

.clear-init:
	@rm -rf .init

init: .clear-init .init

run-app: .init
	@echo "Starting app"
	poetry run uvicorn app.main:app

.cluster-up:
	@echo "Starting cluster. You must have kind installed!"
	kind create cluster --name demo-app-cluster
	@touch .cluster-up

cluster-down:
	@rm -rf .cluster-up
	kind delete cluster --name demo-app-cluster || true

cluster-up: cluster-down .cluster-up

deploy: .cluster-up
	@echo "Deploying into cluster. You must have helm & kubectl installed!"
	helm uninstall --kube-context kind-demo-app-cluster demo-app || true
	helm install --kube-context kind-demo-app-cluster demo-app ./ops/charts
