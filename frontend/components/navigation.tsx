"use client"

import Link from "next/link"
import { usePathname } from "next/navigation"
import { Bot } from "lucide-react"
import { cn } from "@/lib/utils"

export function Navigation() {
  const pathname = usePathname()

  const links = [
    { href: "/", label: "Home" },
    { href: "/about", label: "About" },
    { href: "/app", label: "Identify" },
  ]

  return (
    <nav className="bg-background/90 backdrop-blur-md sticky top-0 z-50 border-b border-border/50">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16 lg:h-20">
          <Link href="/" className="flex items-center gap-2 text-foreground hover:text-primary transition-colors">
            <Bot className="h-6 w-6 lg:h-7 lg:w-7 text-primary" />
            <span className="font-bold text-lg lg:text-xl">I Luv WALL-E</span>
          </Link>

          <div className="flex items-center gap-6 lg:gap-8">
            {links.map((link) => (
              <Link
                key={link.href}
                href={link.href}
                className={cn(
                  "text-sm lg:text-base font-medium transition-colors hover:text-foreground relative",
                  pathname === link.href
                    ? "text-foreground after:absolute after:bottom-[-1.5rem] after:left-0 after:right-0 after:h-0.5 after:bg-primary"
                    : "text-muted-foreground",
                )}
              >
                {link.label}
              </Link>
            ))}
          </div>
        </div>
      </div>
    </nav>
  )
}
