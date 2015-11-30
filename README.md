## Why did you do this?
Frustrated with manually creating a devstack deployment each day, I figured I'd invest a little time now to save a lot later. This is the fruit of my labor.

### Assumptions
You have a DigitalOcean account with an [auth Token](https://cloud.digitalocean.com/settings/applications) handy.

You have [tugboat](https://github.com/pearkes/tugboat) installed and configured. Setup is very easy, just run `tugboat authorize` and you're halfway there.  

### Quick config
After setting up tugboat, make sure to set a default SSH key. You can do this by running `tugboat keys`.

```
Name: tutum-70159d08-bfe8-44de-b0a1-4ce0d2dd9682, (id: 1529470), fingerprint: c4:b0:f2:b0:a7:9f:89:d0:c5:ae:b5:5c:f3:de:a0:69
Name: DO-webserver, (id: 1532126), fingerprint: 37:75:95:7d:93:4f:e0:fd:01:4a:ba:e4:2e:be:6d:c7
```
I want to use DO-webserver in the output above, so my key id is `1532126`. Open up `~/.tugboat` and change `ssh_key` to the key id you retrieved.

## Running the tool
Running the tool is dead easy. Just two steps.  
_DON'T use a shebang, caused a bug in my experience_  
1. `python deploy_stack.py`  
2. Wait for droplet to be created  
3. Run the output command

### Example output
You should see a set of three-ish commands to run, like in the output below. The only difference should be IP address.  
```
Run this: ssh root@162.243.229.80 'bash -s' < stack_setup.sh
Then ssh root@162.243.229.80
then cd /usr/local/src/devstack && su stack
and finally:  ./stack.sh
```

**Typical runtime**: Typical execution time for the `./stack.sh` command is between 1000 to 1400 seconds (16 - 23.5 mins)

Feel free to inspect both scripts to make sure you know what you're installing.

This script does _not_ setup the DD Agent, as my custom Agent download script passes in the API key to my personal account.
