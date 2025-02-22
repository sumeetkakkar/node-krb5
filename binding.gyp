{
    "targets": [{
        "target_name": "krb5",
        "sources": [
            "./src/module.cc",
            "./src/krb5_bind.cc",
            "./src/gss_bind.cc",
            "./src/base64.cc"
        ],
        'cflags!': ['-fno-exceptions'],
        'cflags_cc!': ['-fno-exceptions'],
        'include_dirs': ["<!@(node -p \"require('node-addon-api').include\")"],
        'dependencies': ["<!(node -p \"require('node-addon-api').gyp\")"],
        'cflags!': ['-fno-exceptions'],
        'cflags_cc!': ['-fno-exceptions'],
        'defines': [
          'NAPI_DISABLE_CPP_EXCEPTIONS'
        ],
        "conditions": [
            [
                "OS=='win'",
                {
                    "variables": {
                        "KRB_PATH": "/Program Files/MIT/Kerberos"
                    },
                    "include_dirs": ["<(KRB_PATH)/include", "<(KRB_PATH)/include/gssapi", "src"],
                    "conditions": [
                        [
                            "target_arch=='x64'",
                            {
                                "msvs_settings": {
                                    "VCCLCompilerTool": {
                                        "AdditionalOptions": ["/MP /EHsc"]
                                    },
                                    "VCLinkerTool": {
                                        "AdditionalLibraryDirectories": ["<(KRB_PATH)/lib/amd64/"]

                                    }
                                },
                                "libraries": ["-lkrb5_64.lib", "-lgssapi64.lib"]
                            }
                        ],
                        [
                            "target_arch=='ia32'",
                            {
                                "msvs_settings": {
                                    "VCCLCompilerTool": {
                                        "AdditionalOptions": ["/MP /EHsc"]
                                    },
                                    "VCLinkerTool": {
                                        "AdditionalLibraryDirectories": ["<(KRB_PATH)/lib/amd64/"]

                                    }
                                },
                                "libraries": ["-lkrb5_32.lib", "-lgssapi32.lib"]
                            }
                        ]
                    ]
                }
            ],
            [
                "OS!='win'",
                {
                    "libraries": ["-lkrb5", "-lgssapi_krb5"]
                }
            ]
        ]
    }]
}
