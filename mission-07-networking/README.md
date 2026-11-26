# Mission 07 — How computers communicate

## 1. Task / objective
Describe network concepts, observe a public DNS lookup and connectivity check, and explain a browser request.

## 2. Work completed
| Concept | Reference explanation | Example |
|---|---|---|
| LAN | Network covering a small area | Home or classroom network |
| MAN | Network spanning a city or large campus | City-wide network |
| WAN | Network spanning large geographic areas | The Internet |
| DNS | Finds network addresses associated with domain names | Resolving `example.com` |
| Router | Forwards traffic between networks | Home router connecting devices to an ISP |
| Protocol | Shared rules for communication | HTTPS |
| Packet switching | Sends data in packets that can travel independently | Web traffic |
| Client-server | A client requests a service; a server responds | Browser and web server |

A browser request generally follows these steps: (1) the user enters a web address; (2) DNS finds an address for the domain; (3) the browser opens a connection through the local network and router; (4) the client and server communicate using protocols such as HTTPS; (5) the server returns page data; (6) the browser renders the response.

A terminal lookup for `example.com` could not run in this restricted workspace: `nslookup` returned a socket “operation not permitted” error, and `ping` could not resolve the name. This is an environment limitation, not proof that the example website is unreachable. No local IP or Wi-Fi information is included.

## 3. Commands / tools used
`nslookup example.com` and `ping -c 3 example.com` were each attempted once; both were blocked by the workspace network restrictions. Do not treat these failed attempts as a successful connectivity observation.

## 4. My understanding
Rewrite the network explanations in your own words and repeat the lookup on your own network if required.

## 5. Difficulties faced
The workspace did not allow the DNS socket operation.

## 6. How I resolved them
The error was recorded, and no local network identifiers were published. The lookup needs to be repeated from an unrestricted Terminal.

## 7. Evidence / files
This README contains reference definitions and the exact safe summary of the failed lookup.

## 8. Commit details
This reference draft still needs your own explanation and a successful local observation before it can count as a completed mission commit.
