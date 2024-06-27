import sys
import boto3


def delete_all_record_in_hosted_zone(route53, hosted_zone_id):
    # List all record sets in the hosted zone
    paginator = route53.get_paginator('list_resource_record_sets')
    source_zone_records = paginator.paginate(HostedZoneId=hosted_zone_id)

    changes = []

    for record_set in source_zone_records:
        for record in record_set['ResourceRecordSets']:
            if record['Type'] != 'NS' and record['Type'] != 'SOA': 
                change = {
                    'Action': 'DELETE',
                    'ResourceRecordSet': record
                }
                changes.append(change)

    if changes:
        # Delete record sets in batches if there are changes
        route53.change_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            ChangeBatch={
                'Changes': changes
            }
        )
        print(f"Deleted {len(changes)} record sets.")
    else:
        print("No record sets to delete.")

def main(arg):
    # Create a Route53 client
    route53 = boto3.client('route53')

    # List hosted zone
    hosted_zones = route53.list_hosted_zones().get('HostedZones',[])

    # Search a hosted zone id by name
    for zone in hosted_zones:
        print(zone)
        if zone['Name'][:-1] == arg:
            delete_all_record_in_hosted_zone(route53, zone['Id'])
            try:
                route53.delete_hosted_zone(Id=zone['Id'])
                print(f"Hosted zone {zone['Name']} deleted successfully")
            except Exception as e:
                print(f"Error during delete hosted zone: {e}")
            return
    print("Your hosted zone not found or deleted")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please input your hosted zone name as argument")



