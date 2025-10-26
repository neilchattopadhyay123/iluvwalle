"use client"

import type React from "react"

import { useEffect, useState } from "react"
import useSWR from 'swr'
import { Navigation } from "@/components/navigation"
import { Footer } from "@/components/Footer"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Camera, Upload, Recycle, AlertCircle, CheckCircle2, Info, Trash } from "lucide-react"
import Image from 'next/image'

type RecyclingResult = {
  image: string
  label: string
}

const fetcher = (...args: Parameters<typeof fetch>) =>
  fetch(...args).then(res => res.json());


export default function AppPage() {
  const [result, setResult] = useState<RecyclingResult | null>(null)  
  const { data, error, isLoading } = useSWR('http://127.0.0.1:8000/latest-image', fetcher, { refreshInterval: 1000 })

  useEffect(() => {
    if(error) {
      setResult(null)
    } else if(!isLoading) {
      setResult({image: data.image_base64, label: data.label})
    }
  }, [data, error, isLoading])

  console.log(result)

  return (
    <div className="min-h-screen bg-background">
      <Navigation />

      <div className="bg-gradient-to-br from-primary/20 via-accent/10 to-secondary/20 border-b border-border">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <div className="max-w-4xl mx-auto">
            <div className="text-center">
              <h1 className="text-3xl sm:text-4xl font-bold mb-4">Sensor Dashboard</h1>
              <p className="text-muted-foreground">
                Scan any item to receive sorting instructions.
              </p>
            </div>
          </div>
        </div>
      </div>

      <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="max-w-4xl mx-auto">
          <div className="grid lg:grid-cols-2 gap-8">
            {/* Image Section */}
            <Card className="bg-card">
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Camera className="h-5 w-5 text-primary" />
                  Current Item
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  {!result && (
                    <>
                      <div className="border-2 border-dashed border-border rounded-lg p-12 text-center hover:border-primary/50 transition-colors">
                        <p className="text-md text-muted-foreground mb-4">No items to be sorted</p>
                      </div>
                      <div className="flex items-start gap-2 text-sm text-muted-foreground bg-muted/50 p-4 rounded-lg">
                        <Info className="h-4 w-4 mt-0.5 flex-shrink-0" />
                        <p>
                          For best results, ensure the item is clearly visible and well-lit. Our AI works with bottles,
                          cans, paper, cardboard, and more.
                        </p>
                      </div>
                    </>
                  )}

                  {result && (
                    <div className="relative w-full aspect-square overflow-hidden rounded-lg">
                      <Image
                        src={`data:image/png;base64,${result.image}`}
                        alt={result.label}
                        fill
                        className="object-contain"
                      />
                    </div>
                  )}
                </div>
              </CardContent>
            </Card>

            {/* Results Section */}
            <Card className="bg-card">
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Recycle className="h-5 w-5 text-primary" />
                  Recycling Information
                </CardTitle>
              </CardHeader>
              <CardContent className="flex flex-col items-center justify-center text-center h-full">
                {!result && (
                  <div className="flex flex-col items-center justify-center py-4 text-center">
                    <AlertCircle className="h-12 w-12 text-muted-foreground mb-4" />
                    <p className="text-muted-foreground">
                      Place item in front of sensor to see recycling instructions
                    </p>
                  </div>
                )}

                {result && (
                  <div className="flex flex-col items-center justify-center py-4 text-center">
                    {result.label === "Not Recyclable" ? (
                      <>
                        <Trash className="h-32 w-32 text-primary mb-4" />
                        <h2 className="text-muted-foreground text-xl">
                          Place item in the{" "}
                          <span className="text-primary">
                            <strong>Trash</strong>
                          </span>
                        </h2>
                      </>
                    ) : (
                      <>
                        <Recycle className="h-32 w-32 text-primary mb-4" />
                        <h2 className="text-muted-foreground text-xl">
                          Place item in the{" "}
                          <span className="text-primary">
                            <strong>{result.label}</strong>
                          </span>{" "}
                          recycling bin
                        </h2>
                      </>
                    )}
                  </div>
                )}
              </CardContent>
            </Card>
          </div>

          <Card className="mt-8 bg-gradient-to-br from-primary/5 via-accent/5 to-secondary/5 border-primary/20">
            <CardContent>
              <div className="flex items-start gap-3">
                <Info className="h-5 w-5 text-primary flex-shrink-0 mt-0.5" />
                <div className="space-y-2 text-sm text-muted-foreground">
                  <p className="font-medium text-foreground">Reminder:</p>
                  <ul className="space-y-1 list-disc list-inside">
                    <li>Sorting guidelines may vary by location</li>
                    <li>Always verify with your local waste management facility</li>
                    <li>When uncertain, ask for guidance—every correct sort matters</li>
                  </ul>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>

      {/* Footer */}
      <Footer />
    </div>
  )
}
