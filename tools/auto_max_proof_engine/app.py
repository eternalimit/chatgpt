import streamlit as st
from pathlib import Path
import hashlib, json, datetime, zipfile, tempfile

st.set_page_config(page_title="AUTO MAX Proof Engine", page_icon="•", layout="wide")
st.title("AUTO MAX Proof Engine")
st.caption("Artifact → SHA-256 → UPID → Timestamp → Receipt → Sealed Package")

uploaded = st.file_uploader("Choose an artifact")

if uploaded is not None:
    data = uploaded.getvalue()
    sha256 = hashlib.sha256(data).hexdigest()
    upid = f"AUTO-{sha256[:12].upper()}"
    ts = datetime.datetime.now(datetime.timezone.utc).isoformat()

    col1, col2 = st.columns(2)
    with col1:
        st.metric("SHA-256", sha256)
    with col2:
        st.metric("UPID", upid)

    manifest = {
        "engine": "AUTO MAX Proof Engine",
        "state": 1,
        "anchor": "•",
        "bind": "379999",
        "artifact_name": uploaded.name,
        "artifact_size_bytes": len(data),
        "sha256": sha256,
        "upid": upid,
        "timestamp_utc": ts,
        "verification_status": {
            "artifact_integrity": "recorded",
            "external_signature": False,
            "blockchain_receipt": False,
            "legal_ownership": False
        },
        "evidence_rule": "No conclusion may exceed the evidence attached to the record."
    }

    st.subheader("Receipt")
    st.json(manifest)

    receipt_bytes = json.dumps(manifest, indent=2, ensure_ascii=False).encode("utf-8")

    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        artifact_path = td / uploaded.name
        manifest_path = td / "receipt.json"
        sums_path = td / "SHA256SUMS.txt"
        zip_path = td / f"{upid}_SEALED.zip"

        artifact_path.write_bytes(data)
        manifest_path.write_bytes(receipt_bytes)
        sums_path.write_text(
            f"{sha256}  {uploaded.name}\n"
            f"{hashlib.sha256(receipt_bytes).hexdigest()}  receipt.json\n",
            encoding="utf-8"
        )

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
            z.write(artifact_path, arcname=artifact_path.name)
            z.write(manifest_path, arcname=manifest_path.name)
            z.write(sums_path, arcname=sums_path.name)

        package_bytes = zip_path.read_bytes()

    st.download_button(
        "Download sealed evidence package",
        data=package_bytes,
        file_name=f"{upid}_SEALED.zip",
        mime="application/zip"
    )

    st.info(
        "This package proves the recorded bytes and metadata only. "
        "It does not by itself prove legal ownership, payment, wallet control, or blockchain execution."
    )
else:
    st.write("Upload a file to generate its proof package.")
