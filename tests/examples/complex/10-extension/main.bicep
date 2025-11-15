// https://docs.azure.cn/en-us/azure-resource-manager/bicep/bicep-extension

// Simple extension
extension microsoftGraphV1

// Extension with config and alias
extension kubernetes with {
  namespace: 'default'
  kubeConfig: 'someKubeConfig'
} as k8s
