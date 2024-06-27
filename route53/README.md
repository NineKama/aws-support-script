
# Hosted Zone Cleanup Script

This script deletes all records within a specified hosted zone and then deletes the hosted zone itself in AWS Route 53. The script takes the hosted zone name as an input.

## Prerequisites

1. **Python 3.x**: Ensure you have Python 3.x installed on your machine.
2. **Boto3**: The AWS SDK for Python. Install it using pip:
    ```sh
    pip install boto3
    ```
3. **AWS Credentials**: Ensure your AWS credentials are configured. You can set them up using the AWS CLI or by setting environment variables.

## Usage

1. **Clone the repository or download the script**:
    ```sh
    git clone https://github.com/NineKama/aws-support-script
    cd route53
    ```

2. **Install required packages**:
    ```sh
    pip install boto3
    ```

3. **Run the script**:
    ```sh
    python aws-route53-delete-hosted-zone.py example.com
    ```

## Script Details

### `aws-route53-delete-hosted-zone.py`

This script performs the following actions:

1. **List all record sets in the specified hosted zone** (excluding `NS` and `SOA` records).
2. **Delete all record sets**.
3. **Delete the hosted zone**.


## Notes

- **Safety**: Be very careful when running this script as it will permanently delete DNS records and the hosted zone.
- **Permissions**: Ensure your AWS user has the necessary permissions to list, delete record sets, and delete hosted zones in Route 53.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need for automated cleanup of AWS Route 53 hosted zones.
