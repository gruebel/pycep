// https://docs.azure.cn/en-us/azure-resource-manager/bicep/bicep-import#import-variables-types-and-functions
// https://docs.azure.cn/en-us/azure-resource-manager/bicep/bicep-import#import-namespaces

// simple import
import {myConstant} from '../exports.bicep'
import { myObjectType, sayHello } from 'exports.bicep'

// alias import
import {kubernetes as k8s } from 'exports.bicep'
import { pandas as pd, networkx as nx } from 'exports.bicep'

// mixed import
import { identityPrefixes as prefixes , tagsType } from '../../configuration/shared/shared.bicep'

// wildcard import
import * as myImports from 'exports.bicep'

// namespace import
import 'az@1.0.0'
import 'sys@1.0.0'
