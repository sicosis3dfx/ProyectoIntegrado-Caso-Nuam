import React from 'react';

export const Footer: React.FC = () => {
  return (
    <footer className="nuam-app-footer">
      <div className="footer-centered-container">
        <div className="footer-line-primary">
          <span className="footer-brand font-semibold text-accent">nuam EXCHANGE GROUP</span>
          <span className="footer-bullet">·</span>
          <span>Holding Bursátil Regional (Chile · Perú · Colombia)</span>
        </div>

        <div className="footer-line-secondary">
          <span>Supervisado por CMF, SMV y SFC</span>
          <span className="footer-bullet">·</span>
          <span>DJ 1949 / DJ 1922 SII</span>
          <span className="footer-bullet">·</span>
          <span>🔒 Certificación ISO/IEC 27001</span>
          <span className="footer-bullet">·</span>
          <span>Ley N° 21.719</span>
          <span className="footer-bullet">·</span>
          <span className="footer-version font-mono">v3.2.0-LTS</span>
        </div>
      </div>
    </footer>
  );
};
