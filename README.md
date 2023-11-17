# HitchHiker API Requirements

(See sub-folders for implementations & relevant README docs)

## Store Metrics on WiFi Router

- **Objective:** Store metrics on WiFi Router USB storage.
- **Method:** Use a small local server in Python to receive data on the [count.ly](http://count.ly/) endpoints.
- **Reference:** An [initial example server](https://github.com/kevgibbs/imagine-worldwide/blob/main/analytics_cache.py) is provided.

## Test Application Setup

- **Test App:** Use the test app [countly_test.apk](https://github.com/kevgibbs/imagine-worldwide/raw/main/countly_test.apk) (named “Michal”) on Android.
- **Configuration:** To use HTTP, set up `dnsmasq` or a similar resolver. Point `countly.data.befit.mw` to your test server's address.
- **Note:** This step is needed due to Android's cleartext HTTP restrictions.

## MetricsLocal Server

- **Task:** Implement a server on the WiFi router named “MetricsLocal”.
- **Function:** This server should replicate the functions of the provided sample server.

## Unit Testing

- **Requirement:** Add unit tests for the [count.ly](http://count.ly/) upload endpoints.

## HitchhikerSource gRPC API

- **Build the API:** Implement the following commands:
  - `GetSourceId() -> SourceId`
  - `GetDownloads(ClientId, DestinationId) -> FileList[]`
  - `DownloadFile(ClientId, FileList[]) -> File[]{fileid, filename, type, blob}`
  - `MarkDelivered(ClientId, DestinationId, FileList[])`

### API Functions

- **GetSourceId:** Returns a `SourceId` string (e.g., "pilot04").
- **GetDownloads:** Accepts `ClientId` and `DestinationId`, returns a file list.
- **DownloadFile:** Allows a client to download files.
- **MarkDelivered:** Indicates successful file delivery; the file is then deleted.

### File Structure

- **Proto Structure:** Composed of `fileid` (md5 sum), `filename`, `type`, and an optional `blob`.

## Implementation Notes

- **Use grpclib:** Implement using [Python gRPC](https://github.com/vmagamedov/grpclib) for convenience on the router.

## Data Management

- **Garbage Collection:** Automatically manage metrics based on a configurable size limit (in MB).
- **Process:** Run the garbage collector periodically and delete files in reverse-chronological order.

## Testing Environment

- **~~Test on OpenWRT:** Use an OpenWRT virtual machine for testing.~~

---

## LICENSE

Apache 2.0
