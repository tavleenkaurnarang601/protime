import './globals.css';
import type { Metadata } from 'next';
export const metadata: Metadata={title:'PRO TIME TRACKER',description:'Track Time. Measure Progress. Work Smarter.'};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en"><body>{children}</body></html>}