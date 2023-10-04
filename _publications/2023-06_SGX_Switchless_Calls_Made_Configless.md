---
title: "SGX Switchless Calls Made Configless"
collection: publications
permalink: /publication/2023-06_SGX_Switchless_Calls_Made_Configless
excerpt: 'This paper designs a runtime that allows efficient switchless calls for Intel SGX.'
date: 2023-06-27
venue: 'Proceedings of DSN (53rd IEEE/IFIP DSN)'
paperurl: 'https://arxiv.org/abs/2305.00763'
citation: 'Peterson Yuhala, Michael Paper, Timothée Zerbib, Pascal Felber, Valerio Schiavoni, Alain Tchana (2023). &quot;SGX Switchless Calls Made Configless.&quot; <i>Proceedings of DSN 2023 (53rd IEEE/IFIP DSN)</i>.'
---

Intel's software guard extensions (SGX) provide hardware enclaves to guarantee confidentiality and integrity for sensitive code and data. However, systems leveraging such security mechanisms must often pay high performance overheads. A major source of this overhead is SGX enclave transitions which induce expensive cross-enclave context switches. The Intel SGX SDK mitigates this with a switchless call mechanism for transitionless cross-enclave calls using worker threads. Intel's SGX switchless call implementation improves performance but provides limited flexibility: developers need to statically fix the system configuration at build time, which is error-prone and misconfigurations lead to performance degradations and waste of CPU resources. ZC-SWITCHLESS is a configless and efficient technique to drive the execution of SGX switchless calls. Its dynamic approach optimises the total switchless worker threads at runtime to minimise CPU waste. The experimental evaluation shows that ZC-SWITCHLESS obviates the performance penalty of misconfigured switchless systems while minimising CPU waste. 

[Download paper here](http://tzerbib.github.io/files/DSN23_SGX_switchless_calls_made_configless.pdf)