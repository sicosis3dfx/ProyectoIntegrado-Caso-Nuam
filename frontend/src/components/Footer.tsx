import React from 'react';

export const Footer: React.FC = () => {
  return (
    <footer className="nuam-app-footer">
      <div className="footer-content">
        <div className="footer-left">
          <span className="footer-brand font-semibold text-accent">nuam EXCHANGE GROUP</span>
          <span className="footer-bullet">·</span>
          <span className="footer-holding">Holding Bursátil Regional (Chile · Perú · Colombia)</span>
        </div>

        <div className="footer-center">
          <span className="footer-regulatory">
            Supervisado por CMF · SMV · SFC | DJ 1949 & DJ 1922 SII
          </span>
        </div>

        <div className="footer-right">
          <span className="footer-compliance">
            🔒 ISO/IEC 27001 · Ley 21.719
          </span>
          <span className="footer-bullet">·</span>
          <span className="footer-version font-mono">v3.2.0-LTS</span>
        </div>
      </div>
    </footer>
  );
};
