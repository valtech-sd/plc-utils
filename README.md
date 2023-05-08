# PLC UTILS

A quick way to run Python scripts on PLCs using the Pylogix library.

## Dependencies

- Docker
- Internet access to download docker images

## Bootsrap

1. Clone this repository
2. Build the Docker Compose stack project with `docker-compose build`
3. Run any scripts with `docker compose run plc-utils python <script.py> <args>`

## Examples

### Read the tag list

```bash
docker compose run plc-utils python read_tag_list.py 192.168.1.1 0
```
## PLC Things

- Standard port is 44818 for Logix PLCs.
- Slot is the particular PLC slot to access (a single cabinet might have multiple slots).

## References

- [Pylogix](https://github.com/dmroeder/pylogix/blob/master/docs/Documentation.md)
