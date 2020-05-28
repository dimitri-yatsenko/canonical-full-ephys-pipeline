# Pipeline for extracellular electrophysiology using Neuropixels probe and kilosort clustering method

Build a full ephys pipeline using the canonical pipeline modules
+ [lab-management](https://github.com/vathes/canonical-lab-management)
+ [colony-management](https://github.com/vathes/canonical-colony-management)
+ [ephys](https://github.com/vathes/canonical-ephys)

This repository provides demonstrations for: 
1. Set up a pipeline using different pipeline modules (see [here](./my_project/init_ephys.py))
2. Ingestion of data/metadata based on:
    + predefined file/folder structure and naming convention
    + predefined directory lookup methods (see [here](./my_project/utils.py))
3. Ingestion of clustering results (built-in routine from the ephys pipeline module)

## Getting started

Clone this repository from [here](https://github.com/vathes/canonical-full-ephys-pipeline)

At the root of the repository folder,
 create a new file `dj_local_conf.json` with the following template:
 
```json
{
  "database.host": "hostname",
  "database.user": "username",
  "database.password": "password",
  "database.port": 3306,
  "connection.init_function": null,
  "database.reconnect": true,
  "enable_python_native_blobs": true,
  "loglevel": "INFO",
  "safemode": true,
  "display.limit": 7,
  "display.width": 14,
  "display.show_tuple_count": true,
  "custom": {
      "database.prefix": "db_",
      "ephys_data_dir": "C:/data/ephys_data_dir"
    }
}
```

Specify database's `hostname`, `username` and `password` properly. 

Specify a `database.prefix` to create the schemas.

Setup your data directory following the convention described below.

## Directory structure and file naming convention

The pipeline presented here is designed to work with the directory structure and file naming convention as followed

```
root_data_dir/
└───subject1/
│   └───session0/
│   │   └───probe0/
│   │   │   │   *imec0.ap.meta
│   │   │   └───ksdir/
│   │   │       │   spike_times.npy
│   │   │       │   templates.npy
│   │   │       │   ...
│   │   └───probe1/
│   │       │   *imec1.ap.meta   
│   │       └───ksdir/
│   │           │   spike_times.npy
│   │           │   templates.npy
│   │           │   ...
│   └───session1/
│   │   │   ...
└───subject2/
│   │   ...
```

+ ***root_data_dir*** is configurable in the `dj_local_conf.json`,
 under `custom/ephys_data_dir` variable
+ the ***subject*** directories must match the identifier of your subjects
+ the ***session*** directories must match the following naming convention:
 
    `*_subject_mmddyy*`  (where `mmddyy` is the date of the session)
    
+ the ***probe*** directories must match the following naming convention:

    `subject_mmddyy*_imec[0-9]` (where `[0-9]` is a one digit number specifying the probe number) 
    
+ a neuropixels meta file is required per probe folder, with the following naming convention:

    `subject_mmddyy*imec[0-9].ap.meta`
    
    
## Populating this pipeline

Once you have your data directory configured with the above convention,
 populating the pipeline with your data amounts to these 3 steps:
 
1. Insert new subjects - modify and run this [script](./my_project/insert_subjects.py) to insert new subjects
2. Import session data - run:

    python my_project/ingestion.py
    
3. Import clustering data and populate downstream analyses - run:

    python my_project/populate.py
    
Rerun step 2 and 3 every time new subjects, sessions or clustering data become available.
In fact, step 2 and 3 can be executed as scheduled jobs
 that will automatically process any data newly placed into the ***root_data_dir***
 