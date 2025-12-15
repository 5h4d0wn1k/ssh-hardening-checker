"""
SSH hardening checklist (static guidance + simple banner check).
"""

from __future__ import annotations

import argparse
import asyncio
from typing import Optional


async def grab_banner(host: str, port: int, timeout: float) -> Optional[str]:
    """
    Grab SSH banner from a remote host.
    
    Connects to the SSH service and reads the initial banner message.
    Uses asyncio for non-blocking I/O.
    
    Args:
        host: Target hostname or IP address.
        port: SSH port number (default 22).
        timeout: Connection timeout in seconds.
        
    Returns:
        Banner string if successful, None if connection fails or no banner received.
    """
    try:
        reader, writer = await asyncio.wait_for(asyncio.open_connection(host, port), timeout=timeout)
        data = await asyncio.wait_for(reader.read(128), timeout=1.0)
        writer.close()
        try:
            await writer.wait_closed()
        except Exception:
            pass
        if data:
            return data.decode(errors="ignore").strip()
    except Exception:
        return None
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description="SSH hardening check (banner + guidance).")
    parser.add_argument("--host", required=True)
    parser.add_argument("--port", type=int, default=22)
    parser.add_argument("--timeout", type=float, default=3.0)
    args = parser.parse_args()

    banner = asyncio.run(grab_banner(args.host, args.port, args.timeout))
    if banner:
        print(f"[+] Banner: {banner}")
    else:
        print("[-] No banner or unreachable.")

    print(
        """
Checklist:
- Disable password auth; use key-based only (PasswordAuthentication no).
- Disable root login (PermitRootLogin no).
- Use strong Kex/MAC/Cipher (per latest OpenSSH defaults).
- Set LoginGraceTime low; MaxAuthTries low.
- Use AllowUsers/AllowGroups to limit.
- Move off default port only as a minor noise-reduction (not security).
"""
    )


if __name__ == "__main__":
    main()
