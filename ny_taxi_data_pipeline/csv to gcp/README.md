# Deploy Prefect Workflow

## build deployment
```bash
prefect deploment build ./gcp/etl_web_to_gcs.py:etl_parent_flow -n "deploying a parameterized ETL"
```

## apply deployment 
```bash
prefect deployment apply etl_parent_flow-deployment.yaml
```

## start work pool
```bash
prefect start --work-queue "default"

```