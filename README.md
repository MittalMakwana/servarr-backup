# 📦 Servarr Backup Tool

A small CLI for backing up Servarr applications to an S3-compatible bucket.

## 📖 Overview

This repository is a fork of the original `servarr-backup` project and includes a few follow-up fixes on top of the upstream work. The most recent maintenance update touched the Sonarr, Radarr, and Prowlarr backup clients, so this README now reflects the current behavior and command-line flow in this fork.

The tool currently supports:

- **Sonarr**
- **Radarr**
- **Prowlarr**
- **S3-compatible storage** for backup retention and cleanup

## ✨ Features

- 🔧 Initialize a local YAML configuration file.
- 📦 Create backups for one or more configured Servarr instances.
- 📋 List backups stored in S3-compatible storage.
- 🗑 Delete a named backup, the latest backup, or backups older than the configured retention period.
- 🔐 Document the current HTTPS request behavior used by the Servarr clients in this fork.

## 🚀 Installation

### Prerequisites

- Python **3.8+**
- `pip`

### Install from a fork

Replace `<owner>` below with the GitHub username or organization that hosts your fork:

```sh
pip install git+https://github.com/<owner>/servarr-backup.git
```

### Install from local source

1. Clone your fork:
   ```sh
   git clone https://github.com/<owner>/servarr-backup.git
   cd servarr-backup
   ```
2. Install the package:
   ```sh
   pip install .
   ```
3. Run the CLI:
   ```sh
   servarr --help
   ```

## 📝 Usage

### Initialize configuration

Create a starter config file in `~/.config/servarr/config.yml`:

```sh
servarr config init
```

To generate a default config without prompts:

```sh
servarr config init --non-interactive
```

Show the current config:

```sh
servarr config show
```

### Create backups

Create backups for all configured instances:

```sh
servarr backup create
```

Limit the run to a specific service type:

```sh
servarr backup create --type sonarr
```

Limit the run to a specific instance name or URL:

```sh
servarr backup create --instance main
```

### List backups

List every backup visible in S3:

```sh
servarr backup ls
```

Filter by service type:

```sh
servarr backup ls --type prowlarr
```

Filter by instance:

```sh
servarr backup ls --instance main
```

### Delete backups

Delete a specific backup by name:

```sh
servarr backup delete prowlarr_backup_v1.18.0.4543_2024.06.22_17.28.57.zip
```

Delete the latest backup for the selected service type or instance:

```sh
servarr backup delete --type radarr --latest
```

Delete backups older than the configured retention period:

```sh
servarr backup delete --retention
```

## 🛠 Configuration

The application stores its configuration in `~/.config/servarr/config.yml`.

### Example `config.yml`

```yaml
backups:
  retention: 90d
  log: true

  starrs:
    lidarr: []
    radarr:
      - name: main
        url: https://radarr.example.com
        api_key: your-radarr-api-key
    readarr: []
    sonarr:
      - name: main
        url: https://sonarr.example.com
        api_key: your-sonarr-api-key
    prowlarr:
      - name: main
        url: https://prowlarr.example.com
        api_key: your-prowlarr-api-key

  destination:
    s3:
      endpoint: https://s3.pub1.infomaniak.cloud
      bucket: servarr
      key:
        access: your-access-key
        secret: your-secret-key
```

## ⚠️ Notes

- The current CLI command implementations handle **Sonarr**, **Radarr**, and **Prowlarr**. The sample config still includes `lidarr` and `readarr` placeholders, but those services are not wired into the backup commands yet.
- The latest maintenance change updated the Servarr HTTP calls to run with `verify=False` on requests made to Sonarr, Radarr, and Prowlarr. If you rely on HTTPS certificate validation, review that behavior before deploying this fork.
- A starter configuration template is also available in `examples/config.yml` if you prefer editing a file instead of walking through the interactive setup.

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
