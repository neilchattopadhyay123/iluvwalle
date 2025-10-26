"use client"
import { Bot } from "lucide-react"

export function Footer() {
  return (
    <footer className="border-t border-border py-8 mt-12">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2">
            <Bot className="h-5 w-5 text-primary" />
            <span className="font-semibold">I Luv WALL-E</span>
          </div>
        </div>
      </div>
    </footer>
  )
}